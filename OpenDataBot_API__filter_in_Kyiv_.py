# coding: cp1251
import OpenDataBotAPIviaParse
from bs4 import BeautifulSoup as BS

codes = []

#INPUT
with open('db\Аркуш1.html', 'r') as htmlDB:
    contents = htmlDB.read()
    soup = BS(contents, 'html.parser')

    soup = soup.find_all('td', class_='s4')
    for el in soup:
        codes.append(el.get_text())
    codes = list(filter(None, codes))

def FilterIfItCanBeOurClient(codes):
    checkedCodes = []
    for one in codes:
        # Створіть екземпляр класу OpenDataBotShortNote
        testCompany = OpenDataBotAPIviaParse.OpenDataBotShortNote(one)

        # Створіть екземпляр класу OpenDataBotAPI
        api_instance = OpenDataBotAPIviaParse.OpenDataBotAPI(testCompany)

        address = api_instance.getAddress(testCompany)

        if "Київ" or "Київська" == address:
            checkedCodes.append(testCompany.code)

    return checkedCodes

codes = FilterIfItCanBeOurClient(codes)

#OUTPUT
with open('test2.txt', 'w') as f:
    for i in codes:
        f.write(i + '\n')

