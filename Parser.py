# coding: cp1251
import requests
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent
import time

client = UserAgent()

def soup(url, max_retries=50, initial_delay=1):
    retries = 0
    delay = initial_delay
    while retries < max_retries:
        try:
            time.sleep(delay)  # Затримка перед наступною спробою
            response = requests.get(
                url,
                headers={'client': client.random},
                cookies={}
            )

            # Перевірка статус-коду
            if response.status_code == 200:
                return BS(response.content, 'html.parser')
            else:
                print(f"Помилка при запиті. Спроба {retries + 1}/{max_retries}")
                retries += 1
                delay += 1  # Збільшення затримки на 1 секунду при кожній спробі
        except Exception as e:
            print(f"Помилка: {e}")
    
    print("Не вдалося виконати запит")
    return None



