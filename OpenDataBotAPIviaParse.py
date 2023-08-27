# coding: cp1251
import requests
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent
import re
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
    
class OpenDataBotShortNote():
    code = ''
    name = ''
    address = ''
    phones = []
    emails = []
    registered = False

    def __init__(self, code):
        code = str(code)
        url = 'https://opendatabot.ua/c/' + code + '?from=search'
        page = soup(url)
        self.code = code
        if(page is not None): #FIX CRITERIOUS OF FINDING STATMENTS VALUE?
            self.name = page.find('h1').get_text()
            self.address = page.find_all(class_='col-12 col print-responsive', limit=3)[2].find('p').get_text()

            # ������� �� ����, �� ������� href ���������� � "tel:"
            phone_links = page.find_all('a', href=re.compile(r'^tel:'))

            self.phones = []

            # �������� ������ �������� � �������� href � ������� �� �� ������
            for link in phone_links:
                phone_number = link['href'].replace('tel:', '')
                self.phones.append(phone_number)

            # ������� �� ������� ������ ��������
            #for number in phone_numbers:
            #    print("Phone number:", number)

            #self.emails = page.find(class_='col-sm-4 col-6 col print-responsive').find('p').get_text()

            records = page.find_all(class_='col-sm-4 col-6 col print-responsive')

            email_pattern = re.compile(r'\S+@\S+')
            for p in records:
                text = p.get_text()
                if re.search(email_pattern, text):
                    self.emails = re.search(email_pattern, text).group()
            
            # ��������� �� ��� ������� � �����
            for record in records:
                # ����������, �� ������ �������� ����� ����� "������������"
                if "������������" in record.find('p').get_text():
                    self.registered = True
                    break  # ���� ��������, ����� ��������� ����
    
class OpenDataBotLongNote(OpenDataBotShortNote):
    updatedTime = ""
    establishmentDate = ""
    director = ""
    managers = ""
    state = ""
    typeOfActivity = ""
    VATPayer = False
    