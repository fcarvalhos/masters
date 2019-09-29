import csv
import os
import lizard
import subprocess
import numpy as np


def complexity_analyzer(origin, destiny):
    old_user = ""
    header = 'sumNLOC, sumCCN, sumToken, sumPARAM, sumLength\n0,0,0,0,0\n'
    for root, dirs, files in os.walk(origin):
        for name in files:
            atv_folder = str(root).split("\\")
            atv_folder = atv_folder[5].split("\\")
            atv_folder = str(atv_folder[0])

            atv_folder_path = str(destiny)+"/"+str(atv_folder)
            #atv_folder_path = os.path.join(root,atv_folder)

            if(not os.path.exists(atv_folder_path)):
                os.makedirs(atv_folder_path)


            user = name.split("_")
            #student_folder_path = os.path.join(atv_folder_path, user[0])
            #student_folder_path = str(atv_folder_path)+"/"+str(user[0])
            #if (not os.path.exists(student_folder_path)):
                #os.makedirs(student_folder_path)
            #new_file_name = str(student_folder_path)+"/"+str(user[0])+".csv"
            new_file_name = str(atv_folder_path)+"/"+str(user[0])+".csv"
            with open(new_file_name, "a", newline='\n') as atv_file:

                new_features = []

                #atv_file.write("NLOC,CCN,token,PARAM,length,location,file,function,long_name,start,end,grade\r\n")
                subp_output = subprocess.Popen('lizard --csv '+str(os.path.join(root,name)), stdout=subprocess.PIPE)
                output = subp_output.stdout.read()
                info = output.decode('ascii')
                newLine = info.split("\r\n")

                for i in range(len(newLine)):
                    if newLine[i] is not "":
                        features = newLine[i].split(",")
                        #new_features.append([newLine[i].split(",")[0], newLine[i].split(",")[1], newLine[i].split(",")[2],newLine[i].split(",")[3], newLine[i].split(",")[4]])
                        new_features.append([features[0], features[1], features[2], features[3], features[4]])

                if user[0] != old_user:
                    old_user = user[0]
                    atv_file.write(header)

                if info is not "":
                    sep = np.array(new_features)
                    sep = sep.astype('int32')

                    array_sum = np.sum(sep, axis=0)

                    totalNLOC = array_sum[0]
                    totalCCN = array_sum[1]
                    totalTOKENS = array_sum[2]
                    totalPARAM = array_sum[3]
                    totalLENGTH = array_sum[4]

                    data = (str(totalNLOC)+","+str(totalCCN)+","+str(totalTOKENS)+","+str(totalPARAM)+","+str(totalLENGTH)+"\n")
                    atv_file.write(data)




origin = "mypath\\moodle_Final"
destiny = "destiny_path\\Complexity"

complexity_analyzer(origin, destiny)

