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
        day_keys = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб']  # Ключи в том же порядке, что и start_words

        # Составляем регулярные выражения для очистки текста и извлечения доп. информации после запятой
        clean_task_pattern = re.compile(r'[`"*_#]')
        additional_info_pattern = re.compile(r',\s*(.*)')  # Захватываем текст после запятой

        for i, day_section in enumerate(all_days):
            header = day_section.find(class_="dnevnik-day__header")
            lessons = day_section.find_all(class_="dnevnik-lesson")

            # Используем правильный ключ из day_keys для текущего дня
            day_name = day_keys[i]
            if header:
                # Получаем текст дня недели и дополнительную информацию после запятой
                header_text = header.get_text(strip=True)
                additional_info = additional_info_pattern.search(header_text)
                
                # Добавляем название дня и дополнительные слова после запятой
                day_data[day_name].append(
                    f"*{day_name}*{', ' + additional_info.group(1) if additional_info else ''}\n"
                )
            
            # Обрабатываем уроки
            for lesson in lessons:
                subject = lesson.find(class_="js-rt_licey-dnevnik-subject")
                home_task = lesson.find(class_="dnevnik-lesson__hometask")
                
                if subject and home_task:
                    # Чистим текст и добавляем в вывод
                    subject_text = subject.get_text(strip=True)

                    # Извлекаем текст и ссылку из home_task
                    home_task_text = home_task.get_text(strip=True)  # Текст задания
                    link = home_task.find('a')  # Предполагаем, что ссылка находится в теге <a>

                    if link:
                        url = link.get('href')  # Получаем значение атрибута href
                        home_task_text = clean_task_pattern.sub('dsaddasdasasd', home_task_text)
                        # Удаляем текст ссылки
                        home_task_text = re.sub(r'\s*https?://\S+', '', home_task_text)
                        home_task_text += f" [ссылка]({url})"  # Добавляем ссылку в нужном формате
                    
                    day_data[day_name].append(f"*{subject_text}* - {home_task_text}\n\n")
        
        # Формируем финальную строку для выбранного дня
        result = ''.join(day_data.get(day, []))
        
        end_time = time.time()
        logging.info(f'Асинхронный table: {end_time - start_time:.2f}')
        return result
