import requests
from bs4 import BeautifulSoup

def parse_doctors():
    url = "https://медицинский-сайт.ru/doctors"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # парсинг данных...