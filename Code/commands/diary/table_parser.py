from bs4 import BeautifulSoup
from .diary_parser import ReqSet
import logging
import re


class TableParser(ReqSet):
    def table(self, day: str):
        link = "https://edu.gounn.ru/journal-app/u.1179/week.1"
        
        try:
            response = self.main_session.get(link, headers = self.header)
            logging.info(f"Ответ от страницы с заданием: {response.status_code}")
        except Exception as _ex:
            logging.error(f'cant get access to lesson week: {_ex}')
        
        soup = BeautifulSoup(response.text, 'lxml')
        
        
        all_days = soup.find_all(class_ = 'dnevnik-day')
        
        full_in_one = []
        
        for a in all_days:
            headers = a.find_all(class_ = "dnevnik-day__header") #find all headers
            lessons = a.find_all(class_ = "dnevnik-lesson") # find all lessons
            task_exist = a.find_all(class_ = "dnevnik-lesson__task")
            
            for b in headers:
                if task_exist:
                    full_in_one.append('*'+re.sub(r',.*', '', b.get_text(strip=True))) #returns days ONLY if homework exists on them
                    full_in_one.append(' '+re.sub(r'.*,\s*', '', b.get_text(strip=True)+'*\n'))
                
            
            for c in lessons:
                lesson_name = c.find_all(class_ = "js-rt_licey-dnevnik-subject")
                lesson_home_task = c.find_all(class_ = "dnevnik-lesson__hometask")
                
                for d in lesson_name:
                    if lesson_home_task:
                        full_in_one.append('*'+d.get_text(strip=True)+'* - ')#print(d.text.replace('\n', ''))
                
                for e in lesson_home_task:
                    full_in_one.append(re.sub(r'http[s]?://\S+', ' (ссылка удалена)', e.get_text(strip=True).replace('`', '').replace('"', '')+'\n\n'))
        
        
        start_words = ['*Понедельник', '*Вторник', '*Среда', '*Четверг', '*Пятница']
        end_words = ['*Вторник', '*Среда', '*Четверг', '*Пятница']
        
        ind = full_in_one.index
        
        start_index = [ind(start_words[0]), ind(start_words[1]), ind(start_words[2]), ind(start_words[3]), ind(start_words[4])]
        end_index = [ind(end_words[0]), ind(end_words[1]), ind(end_words[2]), ind(end_words[3])]
        
        
        monday = full_in_one[start_index[0]:end_index[0]]
        tuesday = full_in_one[start_index[1]:end_index[1]]
        wednesday = full_in_one[start_index[2]:end_index[2]]
        thursday = full_in_one[start_index[3]:end_index[3]]
        friday = full_in_one[start_index[4]:]
        
        no_list1 = ''.join(monday)
        no_list2 = ''.join(tuesday)
        no_list3 = ''.join(wednesday)
        no_list4 = ''.join(thursday)
        no_list5 = ''.join(friday)
            
        
        if day == 'Пн':
            return no_list1
        if day == 'Вт':
            return no_list2
        if day == 'Ср':
            return no_list3
        if day == 'Чт':
            return no_list4
        if day == 'Пт':
            return no_list5