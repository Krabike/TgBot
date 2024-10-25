import requests
import fake_useragent
import re
from bs4 import BeautifulSoup


class ReqSet:
    def __init__(self):
        self.session = requests.Session()
        self.user = fake_useragent.UserAgent().random

        self.lessons_week = "https://edu.gounn.ru/journal-app/u.1179/week.0"

        self.header = {
        "user-agent": self.user
        }    
        self.data = {
            "username": "",
            "password": "",
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
    def notes(self):
        r = self.main_session.head('https://edu.gounn.ru/journal-user-preferences-esia-action/?action=lately&hash=d89c2af7296611982180d72ddc76d71a')
        print(r)
        lessons_response = self.main_session.get(self.lessons_week, headers = self.header).text
        
        soup = BeautifulSoup(lessons_response, 'lxml')
        
        days = soup.find_all(class_ = "dnevnik-day")[0:5] #get all days
        
        week = []
        for i in days:
            headers = i.find_all(class_ = "dnevnik-day__header")
            for x in headers:
                week.append('\n***' + x.get_text(strip=True) + '***\n') #get day header
        
            lesson = i.find_all(class_ = "dnevnik-lesson")
            for b in lesson:
                notes_day = b.find_all(class_ = "js-rt_licey-dnevnik-subject")
                
                for m in notes_day:
                    notes = b.find_all(class_ = "dnevnik-mark")
                    if notes:
                        week.append(m.get_text(strip=True)+' - ') #get days ONLY with notes
                        
                    for h in notes:
                        week.append(h.get_text(strip=True)+'\n') #get all notes
                    
        week_final = ''.join(week)
        #print(week_final)
        return week_final  
                
             
#DiaryNotes().notes2() 