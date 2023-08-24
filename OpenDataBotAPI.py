# coding: cp1251
import requests
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent

client = UserAgent()

def soup(url):
    response = requests.get(
        url,
        headers = {'client': client.random}
    )
    return BS(response.content, 'html.parser')
    
class OpenDataBotShortNote():
    code = '0'
    name = 'ТОВ "ТЮЛЬПАН"'
    address = 'Київ'
    phones = '+380000000000'
    email = 'some@email.com'
    def __init__(self, code):   #needDEBUG
        code = str(code)
        url = f"https://opendatabot.ua/c/{code}?from=search"
        soup(url)
        self.code = code
        self.name = soup.find('h1').get_text()
        self.address = soup.find_all(class_='col-12 col print-responsive', limit=3)[2].find('p').get_text()
        self.phones = soup.find_all(class_='col-12 col print-responsive', limit=4)[3].find('a').get_text() #takeOnePhone(needDEBUG)
        self.email = soup.find(class_='col-sm-4 col-6 col print-responsive').find('p').get_text()
        
    
class OpenDataBotNote(OpenDataBotShortNote):
    updatedTime
    establishmentDate
    director
    managers
    state
    typeOfActivity
    VATPayer = False
    

class OpenDataBotAPI():
    def __init__(self, code):
        company = OpenDataBotShortNote(code)

    def printInfo(OpenDataBotShortNote):
        pass
    def getAddress(OpenDataBotShortNote):
        pass
    def checkAddress(OpenDataBotShortNote, criterio="Київ"):
        return False
    def __checkInput():
        pass