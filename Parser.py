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
            time.sleep(delay)  # �������� ����� ��������� �������
            response = requests.get(
                url,
                headers={'client': client.random},
                cookies={}
            )

            # �������� ������-����
            if response.status_code == 200:
                return BS(response.content, 'html.parser')
            else:
                print(f"������� ��� �����. ������ {retries + 1}/{max_retries}")
                retries += 1
                delay += 1  # ��������� �������� �� 1 ������� ��� ����� �����
        except Exception as e:
            print(f"�������: {e}")
    
    print("�� ������� �������� �����")
    return None



