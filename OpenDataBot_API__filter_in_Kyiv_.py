# coding: cp1251
import OpenDataBotAPIviaParse
from bs4 import BeautifulSoup as BS
import pandas as pd

codes = []

#INPUT
with open('db\input\Аркуш1.html', 'r') as htmlDB:
    contents = htmlDB.read()
    soup = BS(contents, 'html.parser')

    soup = soup.find_all('td', class_='s4')
    for el in soup:
        codes.append(el.get_text())
    codes = list(filter(None, codes))
    
    #DEBUG
    print('WE GOT INPUT\n')


# Створення порожнього DataFrame з відповідними стовпчиками
columns = ['code', 'name', 'email', 'phones', 'address', 'registered']
df = pd.DataFrame(columns=columns)
#DEBUG
print('DataFrame was created\n')

def AddCompanyToDataFrame(code, name, emails, phones, address, registered):
    phones_str = ', '.join(phones)  # З'єднати всі номери телефонів в одному рядку
    emails_str = ', '.join(emails)  # З'єднати всі електронні пошти в одному рядку
    new_row = pd.Series({'code': code, 'name': name, 'email': emails_str, 'phones': phones_str, 'address': address, 'registered': registered})
    # Додати новий рядок до існуючого DataFrame
    global df
    df = df.append(new_row, ignore_index=True)
    #DEBUG
    print('company was added')

def SavePotentialClients(codes):
    global df
    for one in codes:
        # Створіть екземпляр класу OpenDataBotShortNote
        testCompany = OpenDataBotAPIviaParse.OpenDataBotShortNote(one)
        #DEBUG
        print(f'-----------{testCompany.code}')

        if "Київ" in testCompany.address or "Київська" in testCompany.address:
            if testCompany.registered:
                print(testCompany.code + '\t is ' + str(testCompany.registered))

                AddCompanyToDataFrame(
                    testCompany.code,
                    testCompany.name,
                    testCompany.emails,
                    testCompany.phones,
                    testCompany.address,
                    testCompany.registered
                )
                # Додайте дані до існуючого файлу CSV у режимі додавання ('a')
                with open('db\output\output.csv', 'a', newline='') as csv_file:
                    df.to_csv(csv_file, mode='a', header=not csv_file.tell(), index=False)

    df.to_csv('db\output\outputFromDF.csv', index=False)
    #DEBUG
    print('OUTPUT WAS COMPLETED')

SavePotentialClients(codes)
#DEBUG
print('\nFINISH')

