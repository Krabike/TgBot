from bs4 import BeautifulSoup
from diary_parser import ReqSet
import logging

logging.basicConfig(level=logging.INFO)

#Set parol and login into class
class TableParser(ReqSet):
    def table(self):
        link = "https://edu.gounn.ru/journal-app/u.1179/week.-2"
        
        try:
            response = self.main_session.get(link, headers = self.header)
            logging.info(f"Ответ от страницы с заданием: {response.status_code}")
        except Exception as _ex:
            logging.error(f'cant get access to lesson week: {_ex}')
        
        soup = BeautifulSoup(response.text, 'lxml')
        
        
        all_days = soup.find_all(class_ = 'dnevnik-day')
        
        
        for a in all_days:
            headers = a.find_all(class_ = "dnevnik-day__header") #find all headers
            lessons = a.find_all(class_ = "dnevnik-lesson") # find all lessons  #js-rt_licey-dnevnik-subject
            
            for b in headers:
                task_exist = a.find_all(class_ = "dnevnik-lesson__task")
                if task_exist:
                    print('\n'+b.text.replace('\n', '')) #returns days ONLY if homework exists on them
                
            
            for c in lessons:
                lesson_name = c.find_all(class_ = "js-rt_licey-dnevnik-subject")
                lesson_home_task = c.find_all(class_ = "dnevnik-lesson__hometask")
                
                for d in lesson_name:
                    if lesson_home_task:
                        print(d.text.replace('\n', ''))
                
                for e in lesson_home_task:
                    print(e.text.replace('\n', ''))
                
                #print(c.text)
            
        
        
        
        
        #logging.info('work!')

TableParser('DG2009', 'parolpafrol').table()