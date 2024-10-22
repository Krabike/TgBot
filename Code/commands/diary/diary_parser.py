import requests
import fake_useragent
from bs4 import BeautifulSoup
'''
ОБЯЗАТЕЛЬНО ВСЕ ЗАСУНУТЬ В КЛАСС ЧЕРЕЗ ООП
'''

class ReqSet:
    def __init__(self):
        self.session = requests.Session()
        self.user = fake_useragent.UserAgent().random


        self.header = {
        "user-agent": self.user
        }    
        self.data = {
            "username": "DG2009",
            "password": "parolpafrol",
        }


        link = 'https://edu.gounn.ru/ajaxauthorize'
        self.response = self.session.post(link, data = self.data, headers = self.header).text


        self.cookies_dict = [
            {"domain": key.domain, "name": key.name, "path": key.path, "value": key.value}
            for key in self.session.cookies
        ]


        self.main_session = requests.Session()
        for cookies in self.cookies_dict:
            self.main_session.cookies.set(**cookies)


class DiaryNotes(ReqSet):
    def get_notes(self):
        lessons_week = "https://edu.gounn.ru/journal-app/u.1179/week.0"
        lessons_response = self.main_session.get(lessons_week, headers = self.header).text
        soup = BeautifulSoup(lessons_response, 'lxml')
        
        get_notes = soup.find_all(class_ = "dnevnik-mark")
        
        all_notes = []
        for i in get_notes:
            all_notes.append(i.text.replace('\n', '').strip())
            
        all_notes_ready = ', '.join(all_notes)
        return all_notes_ready
        
#print(DiaryNotes().get_notes())