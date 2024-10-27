import requests
import fake_useragent
import logging
from bs4 import BeautifulSoup


logging.basicConfig(level=logging.INFO)
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
            logging.error(f'ошибка при авторизации, ошибка - {_ex}')

        self.cookies_dict = [
            {"domain": key.domain, "name": key.name, "path": key.path, "value": key.value}
            for key in self.session.cookies
        ]


        self.main_session = requests.Session()
        try:
            for cookies in self.cookies_dict:
                self.main_session.cookies.set(**cookies)
            logging.info('cookies seted')
        except:
            logging.info('cookies error')


class DiaryNotes(ReqSet):
    def notes(self):
        lessons_week = "https://edu.gounn.ru/journal-app/u.1179/week.0"
        
        
        lessons_response = self.main_session.get(lessons_week, headers = self.header)
        logging.info(f'овтет от страницы с оценками - {lessons_response.status_code}')
        
        soup = BeautifulSoup(lessons_response.text, 'lxml')
        
        days = soup.find_all(class_ = "dnevnik-day")[0:5] #get all days
        
        week = []
        for i in days:
            lesson = i.find_all(class_ = "dnevnik-lesson")
            headers = i.find_all(class_ = "dnevnik-day__header")
            
            for x in headers:
                notes_exist = i.find_all(class_ = "dnevnik-mark")
                if notes_exist:
                    week.append('\n***' + x.get_text(strip=True) + '***\n') #get day header ONLY with notes
        
            for b in lesson:
                notes_day = b.find_all(class_ = "js-rt_licey-dnevnik-subject") #get lessons
                
                for m in notes_day:
                    notes = b.find_all(class_ = "dnevnik-mark")
                    if notes:
                        week.append(m.get_text(strip=True)+' - ') #get lessons ONLY with notes
                        
                    for h in notes:
                        week.append('_'+h.get_text(strip=True)+'_\n') #get all notes
                    
        week_final = ''.join(week)
        
        logging.info('Финальный вывод')
        
        if week_final == '':
            week_final = '*На этой неделе у тебя нет оценок*'
        #print(week_final)
        return week_final
                
             
#DiaryNotes().notes() 