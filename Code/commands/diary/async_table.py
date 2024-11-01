import time
import logging
import re
from bs4 import BeautifulSoup
from .async_parser import NotesParser

class TableParser:
    async def parser(self, login, password, day: str, week=0):
        start_time = time.time()
        content = await NotesParser().login(login, password, week)
        
        soup = BeautifulSoup(content, 'lxml')
        all_days = soup.find_all(class_='dnevnik-day')

        day_data = {
            'Пн': [], 'Вт': [], 'Ср': [], 'Чт': [], 'Пт': [], 'Сб': []
        }
        day_keys = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб']

        pattern = re.compile(r'[`*_~]')
        days_pattern = re.compile(r',\s*(.*)')

        for i, day_section in enumerate(all_days):
            header = day_section.find(class_="dnevnik-day__header")
            lessons = day_section.find_all(class_="dnevnik-lesson")

            day_name = day_keys[i]
            if header:
                additional_info = days_pattern.search(header.get_text(strip=True))
                
                day_data[day_name].append(
                    f"*{day_name}*{', ' + additional_info.group(1) if additional_info else ''}"
                )
            for lesson in lessons:
                lesson_name = lesson.find_all(class_ = 'js-rt_licey-dnevnik-subject')
                lesson_task = lesson.find_all(class_ = 'dnevnik-lesson__task')
                
                for name in lesson_name:
                    if lesson_task:
                        day_data[day_name].append(f"\n\n*{name.get_text(strip=True)}* - ")

                for task in lesson_task:
                    links = task.find_all(href=True)
                    btn = task.find_all(class_ = 'button__title')
                    for b in btn:
                        b.decompose()
                    
                    task = task.get_text(strip=True)
                    clean = pattern.sub('', task)
                    clean = re.sub(r'\s*https?://\S+', '', clean)
                    
                    day_data[day_name].append(f"{clean}")
                    
                    if links:
                        for d in links:
                            link_url = d.get('href')
                            link_beautiful = f" [ссылка]({link_url}) "
                            day_data[day_name].append(f"{link_beautiful}")
        
        result = ''.join(day_data.get(day, []))
        
        end_time = time.time()
        logging.info(f'Асинхронный парсер table: {end_time - start_time:.2f}')
        return result