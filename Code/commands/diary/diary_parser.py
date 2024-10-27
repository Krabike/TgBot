import requests
import fake_useragent
import logging
from bs4 import BeautifulSoup


class ReqSet:
    def __init__(self, login, password):
        self.session = requests.Session()
        self.user = fake_useragent.UserAgent().random

        self.header = {
        "user-agent": self.user
        }    
        self.data = {
            "username": f"{login}",
            "password": f"{password}",
        }
        

        link = 'https://edu.gounn.ru/ajaxauthorize'
        try:
            self.response = self.session.post(link, data = self.data, headers = self.header).text
            logging.info(f'авторизация успешна')
        except requests.exceptions.RequestException as _ex:
            logging.error(f'authorization: {_ex}')

        self.cookies_dict = [
            {"domain": key.domain, "name": key.name, "path": key.path, "value": key.value}
            for key in self.session.cookies
        ]


        self.main_session = requests.Session()
        try:
            for cookies in self.cookies_dict:
                self.main_session.cookies.set(**cookies)
            logging.info('cookies seted')
        except Exception as _ex:
            logging.error(f'cookies: {_ex}')


class DiaryNotes(ReqSet):
    def notes(self, week = 0):
        lessons_week = f"https://edu.gounn.ru/journal-app/u.1179/week.{week}"
        
        
        try:
            lessons_response = self.main_session.get(lessons_week, headers = self.header)
        except Exception as _ex:
            logging.error(f'cant get access to lesson week: {_ex}')
        logging.info(f'овтет от страницы с оценками - {lessons_response.status_code}')
        
        soup = BeautifulSoup(lessons_response.text, 'lxml')
        
        days = soup.find_all(class_ = "dnevnik-day")[0:6] #get all days
        
        week = []
        for i in days:
            lesson = i.find_all(class_ = "dnevnik-lesson")
            headers = i.find_all(class_ = "dnevnik-day__header")
                
            for x in headers:
                notes_exist = i.find_all(class_ = "dnevnik-mark")
                if notes_exist:
                    week.append('\n\n***' + x.get_text(strip=True) + '***') #get day header ONLY with notes
        
        
            for b in lesson:
                notes_day = b.find_all(class_ = "js-rt_licey-dnevnik-subject") #get lessons
                
                for m in notes_day:
                    notes = b.find_all(class_ = "dnevnik-mark")
                    if notes:
                        week.append('\n'+m.get_text(strip=True)+' - ') #get lessons ONLY with notes
                        
                    for h in notes:
                        week.append('*'+h.get_text(strip=True).replace('\n', ' ')+'* ')#get all notes
                    
        week_final = ''.join(week)
        
        logging.info('Финальный вывод')
        if week_final == '':
            week_final = '*На этой неделе у тебя нет оценок*'
        return week_final