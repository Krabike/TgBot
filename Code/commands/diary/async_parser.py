import fake_useragent
import aiohttp
import asyncio
import time
import logging
from bs4 import BeautifulSoup

class NotesParser:
    async def login(self, login, password, week=0):
        authorize_link = 'https://edu.gounn.ru/ajaxauthorize'
        skip_link = 'https://edu.gounn.ru/journal-user-preferences-esia-action'
        week_link = f'https://edu.gounn.ru/journal-app/u.1179/week.{week}'
        user = fake_useragent.UserAgent().random
        timeout = aiohttp.ClientTimeout(total=10)
        
        async with aiohttp.ClientSession(timeout=timeout) as session:
            header = {
            "user-agent": user
            }
            
            data = {
            "username": f"{login}",
            "password": f"{password}",
            }
            try:
                async with session.post(authorize_link, json = data, headers=header) as authorize_response:
                    logging.info(f'Статус авторизации: {authorize_response.status}')
                    if authorize_response.status == 400:
                        return ''
                    try:
                        async with session.get(skip_link, headers=header) as skip_response:
                            logging.info(f'Статус запроса skip: {skip_response.status}')
                            content = await skip_response.text()
                            soup = BeautifulSoup(content, 'lxml')
                        
                            skip = soup.find(class_ = 'lgray font20 lh24 lgray')
                            skip_href = skip['href']
                        
                            async with session.get(skip_link+skip_href, headers=header) as skip_post:
                                logging.info(f'skip status: {skip_post.status}')
                                
                                async with session.get(week_link, headers=header) as week_response_skip:
                                    logging.info(f'Статус запроса week with skip: {week_response_skip.status}')
                                    self.content = await week_response_skip.text()
                                    return self.content
                    except:
                            async with session.get(week_link, headers=header) as week_response:
                                logging.info(f'Статус запроса week: {week_response.status}')
                                self.content = await week_response.text()
                                return self.content
                        
            except asyncio.TimeoutError as _ex:
                logging.error(f'Timeout NotesParser: {_ex}')

    
    async def parser(self, login, password, week=1):
        time1 = time.time()
        tasks = [self.login(login, password, week)]
        await asyncio.gather(*tasks)
        
        soup = BeautifulSoup(self.content, 'lxml')

        days = soup.find_all(class_ = "dnevnik-day") #get all days
        
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
        
        if week_final == '':
            week_final = '*На этой неделе у тебя нет оценок*'
        time2 = time.time()
        logging.info(f'Асинхронный парсер: {time2-time1}')
        return week_final