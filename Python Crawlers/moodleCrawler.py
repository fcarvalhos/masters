import os

import bs4
import requests
from zipfile import ZipFile
from io import BytesIO


class submission(object):
    pass

class moodle_crawler():
    def __init__(self, username, password, path, links = None):
        if links is None:
            session = self.login(username, password)
            links = self.get_submission_links(session)
        session = self.login(username, password)
        self.get_codes(links, session, path)


    def login(self, username, password):
        # loga no site moodle usando o username e senha passados por parametro
        payload = {'username': username, "password": password}
        session_requests = requests.session()
        login_url = "http://moodle.caed-lab.com/login/index.php"

        result = session_requests.post(
            login_url,
            data=payload,
            headers=dict(referer=login_url)
        )
        return session_requests

    def get_submission_links(self, session_requests):


        #realizar o crawler no site pegando os links relativos as atividades atv_id
        submission_links = []
        atv_id = [493, 496, 497, 504, 498, 515, 454, 457, 520, 522, 528, 524, 478, 534, 538, 542, 544, 545]
        url_base = "http://moodle.caed-lab.com/mod/vpl/views/submissionslist.php?id=%(id_url_atv)s"

        # para cada item em atv_id eh realizado um request e salvo o padrao html parseado em listSoup
        for i in atv_id:
            d = {"id_url_atv": str(i)}
            listR  = session_requests.get(url_base % d, headers={'User-Agent': "Magic Browser"})
            listSoup = bs4.BeautifulSoup(listR.text, "html.parser")
            tds = listSoup.findAll('td', {'class': 'cell c4'})
            #td[i].content[0]['href'] pega o primeiro conteudo da classe cell c4 que contenha href

            #print(listSoup.findAll('td', {'class': 'cell c4'}))
            for student in range(0, len(tds)):
                #print(tds[student].contents[0]['href'])
                submission_links.append(tds[student].contents[0]['href'])

        return submission_links


    def get_codes(self, submission_links, session_requests, path_save):
        for code_link in submission_links:
            listR  = session_requests.get(code_link, headers={'User-Agent': "Magic Browser"})
            listSoup = bs4.BeautifulSoup(listR.text, "html.parser")
            tds = listSoup.findAll('td', {'class': 'cell c1'})
            #td[i].contents[0]['href'] pega o primeiro conteudo da classe cell c4 que contenha href


            for submission in range(0, len(tds)):
                code_submission_link = tds[submission].contents[0]["href"]
                listR = session_requests.get(code_submission_link, headers={'User-Agent': "Magic Browser"})
                listSoup = bs4.BeautifulSoup(listR.text, "html.parser")
                divs = listSoup.findAll('div', {'role': 'main'})
                #divs = listSoup.findAll('div', {'class': 'box generalbox'})
                # recebe o link do arquivo a ser baixado
                for i in range(0, len(divs[0].contents)):
                    try:
                        if str(divs[0].contents[i].contents[0]) == "Download":
                            download_link = divs[0].contents[i]["href"]
                            break
                    except:
                        pass


                #recebe o student ID
                student_id = download_link.split('userid=')[1].split("&submissionid")[0]
                #recebe o submission id
                submission_id = download_link.split("&submissionid=")[1]
                #recebe o id da atividade
                atv_id = download_link.split('?id=')[1].split("&userid")[0]


                #cria as pastas de atividade e dos alunos caso ainda nao tenham sido criadas
                new_folder = path_save + str(atv_id)
                if (not os.path.exists(new_folder)):
                    os.makedirs(new_folder)
                new_folder = path_save + str(atv_id)+"\\"+str(student_id)
                if (not os.path.exists(new_folder)):
                    os.makedirs(new_folder)

                #baixa o arquivo do moodle a partit do link salvo anteriormente
                file_request = session_requests.get(download_link, headers={'User-Agent': "Magic Browser"})
                zipfile = ZipFile(BytesIO(file_request.content))
                zipfile.extractall(new_folder)
                os.rename(new_folder+"\\"+"user.c", new_folder+"\\"+str(student_id)+"_"+str(submission_id)+".c")
                #os.remove(new_folder+"\\"+"user.c")



path_save = <insert path name here (e.g. c:\\userF\\mypath\\)>

my_crawler = moodle_crawler(user_name,password, path_save)



