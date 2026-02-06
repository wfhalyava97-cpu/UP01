import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
from typing import List, Dict
import logging
from urllib.parse import urljoin

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MedicalSiteParser:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        })
    
    def parse_prodoctorov(self) -> List[Dict]:
        """Парсинг сайта prodoctorov.ru"""
        doctors = []
        base_url = "https://prodoctorov.ru"
        
        try:
            # Пример URL (может потребоваться адаптация)
            url = f"{base_url}/moskva/vrach/"
            logger.info(f"Парсинг {url}")
            
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Поиск карточек врачей (селекторы нужно уточнить)
            doctor_cards = soup.find_all('div', class_=re.compile(r'doctor-card|specialist-card'))
            
            for card in doctor_cards[:10]:  # Ограничим 10 врачами для примера
                try:
                    name_elem = card.find('h3') or card.find('a', class_=re.compile(r'name|title'))
                    specialization_elem = card.find('div', class_=re.compile(r'specialization|profession'))
                    
                    if name_elem:
                        doctor_data = {
                            'source_website': 'prodoctorov.ru',
                            'full_name': name_elem.text.strip(),
                            'specialization': specialization_elem.text.strip() if specialization_elem else 'Не указано',
                            'clinic_name': 'Не указано',
                            'address': 'Москва',  # По умолчанию
                            'phone': '',
                            'experience': '',
                            'education': '',
                            'parsed_at': datetime.now().isoformat(),
                            'raw_data': str(card)[:500]  # Сохраняем часть HTML для отладки
                        }
                        
                        # Дополнительная информация
                        experience_elem = card.find(text=re.compile(r'стаж|опыт', re.IGNORECASE))
                        if experience_elem:
                            doctor_data['experience'] = experience_elem.find_next().text if experience_elem.find_next() else experience_elem.text
                        
                        doctors.append(doctor_data)
                        
                except Exception as e:
                    logger.error(f"Ошибка парсинга карточки врача: {e}")
                    continue
            
            logger.info(f"Найдено врачей: {len(doctors)}")
            
        except Exception as e:
            logger.error(f"Ошибка парсинга prodoctorov.ru: {e}")
        
        return doctors
    
    def parse_docmate(self) -> List[Dict]:
        """Парсинг сайта docmate.ru"""
        doctors = []
        # Здесь будет логика парсинга другого сайта
        return doctors
    
    def parse_all_sites(self) -> List[Dict]:
        """Парсинг всех сайтов"""
        all_doctors = []
        
        # Парсим первый сайт
        prodoctorov_doctors = self.parse_prodoctorov()
        all_doctors.extend(prodoctorov_doctors)
        
        # Здесь можно добавить другие сайты
        # docmate_doctors = self.parse_docmate()
        # all_doctors.extend(docmate_doctors)
        
        logger.info(f"Всего собрано врачей: {len(all_doctors)}")
        return all_doctors

if __name__ == "__main__":
    parser = MedicalSiteParser()
    doctors = parser.parse_all_sites()
    
    # Вывод результатов
    for i, doctor in enumerate(doctors, 1):
        print(f"{i}. {doctor['full_name']} - {doctor['specialization']}")