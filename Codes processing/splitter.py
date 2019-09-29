import os
import re

from xml.dom import minidom

fileSource = mypath\mdl_vpl_code_recording_log.xml"
fileG = open(fileSource, "r")


xmldoc = minidom.parse(fileSource)

table_list = xmldoc.getElementsByTagName('table')

#retorna o valor entre as tags do XML

#table_list[0].getElementsByTagName("column")[1].firstChild.nodeValue

#retorna o valor de name = {id, cmid, vpl. userid, datarecorded ou code}

#table_list[0].getElementsByTagName("column")[5].getAttribute("name")

#cria um dict de atividades CMID com todos os alunos e cada aluno (USERID) tem um dict de submissoes

#d -> possui duas chaves atividade e aluno para um id unico, ex: d[522][10227] == id X
d = dict()
#id_dict -> a chave eh o id e o valor eh uma lista de codigos
id_dict = dict()
for t in table_list:

    id = int(t.getElementsByTagName("column")[0].firstChild.nodeValue)
    cmid = int(t.getElementsByTagName("column")[1].firstChild.nodeValue)
    userID = int(t.getElementsByTagName("column")[3].firstChild.nodeValue)
    c = t.getElementsByTagName("column")[5].firstChild.nodeValue.split('"content":"')
    #c =  t.getElementsByTagName("column")[5].firstChild.nodeValue.split('"content":"')[1].split('"},{"fileName"')[0]
    d[cmid] = d.get(cmid, dict())
    d[cmid][userID] = d[cmid].get(userID, list())
    d[cmid][userID].append(id)
    id_dict[id] = list()

    for i in range(1, len(c),2):
        # o incremento de 2 serve para pegar apenas as linhas impares de codigo depois dos splits
        code = c[i].split('"}]},{"startTime":"')[0].split('"}]}]')[0]
        code = code.split('"}\n{"fileName":"input.txt",')[0]
        code = code.split('"},\n{"fileName":"input.txt",')[0]
        code = code.split('"},{"fileName":"input.txt",')[0]


        #platipus eh um placeholder para evitar que o \n que o aluno escreveu na string desapareca do reino dos mortais (Neto, 2019)
        code = code.replace('\\\\n', 'platipusGayAzul@715"')
        code = code.replace('\\n', '\n')
        code = code.replace('platipus@715"', '\\n')
        code = code.replace('\\\\"', 'platipus@715"')
        code = code.replace('\\"', '"')
        code = code.replace('platipus@715"', '\\"')
        code= code.replace('\\\\\\\\', '\\\\')

        #code = code.replace('";', '"')
        #code = code.replace(';"', '"')
        code = code.replace(',{', '\n{')
        #code = code.replace('#include', '\n#include')
        code = code.replace('\\t', '\t')
        code = code.replace('&amp;', '&')
        code = code.replace('\/', '/')
        code = code.replace('\\\\r', 'platipus@715"')
        code = code.replace('\\r', '\r')
        code = code.replace('platipus@715"', '\\r')
        #code = code.replace('"}\n{"fileName":"input.txt",', '')

        id_dict[id].append(code)



# cria as pastas divididas por atividades > usuarios > codigos submetidos
for atv in d.keys():
    #cria pasta da atv cmid

    new_folder = <your path>+str(atv)
    if (not os.path.exists(new_folder)):
        os.makedirs(new_folder)
    for user in d[atv].keys():
        #cria pasta de usuario com nome do user
        user_folder = new_folder+"/"+str(user)
        if (not os.path.exists(user_folder)):
            os.makedirs(user_folder)
        ids = d[atv][user]
        for submission_id in ids:
            for code in id_dict[submission_id]:
                #escreve os codigos contidos em id_dict
                file_name = str(user_folder)+"/"+str(user)+"_"+str(submission_id)+".c"
                new_file = open(file_name, "w")
                new_file.write(code)
                new_file.close()
