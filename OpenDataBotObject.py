# coding: cp1251
import re
import Parser
    
class OpenDataBotShortNote():
    code = ''
    name = ''
    address = ''
    phones = []
    emails = ''
    registered = '?'

    def __init__(self, code):
        code = str(code)
        self.code = code
        url = 'https://opendatabot.ua/c/' + code + '?from=search'
        page = Parser.soup(url)
        try:
            if(page is not None):
                self.name = page.find('h1').get_text()

                cols12 = page.find_all('div', class_='col-12 col print-responsive')
                for col12 in cols12:
                    if re.search(r'\bАдреса\b', col12.contents[1].contents[0]):
                        self.address = col12.find('p').get_text()
                        break

                # Знайдіть всі теги, де атрибут href починається з "tel:"
                phone_links = page.find_all('a', href=re.compile(r'^tel:'))

                self.phones = []

                # Витягніть номери телефону з атрибутів href і додайте їх до списку
                for link in phone_links:
                    phone_number = link['href'].replace('tel:', '')
                    self.phones.append(phone_number)

                # Виведіть всі знайдені номери телефону
                #for number in phone_numbers:
                #    print("Phone number:", number)

                #self.emails = page.find(class_='col-sm-4 col-6 col print-responsive').find('p').get_text()

                records = page.find_all(class_='col-sm-4 col-6 col print-responsive')

                for record in records:
                    if re.search(r'\bПошта\b', record.contents[1].contents[0]):
                        self.emails.append(record.find('p').get_text())
            

                for record in records:
                    if re.search(r'\bСтан\b', record.contents[1].contents[0]):
                        self.registered = record.find('p').get_text()
                        break
            else:
                return None
        except :
            return None
        
    
class OpenDataBotLongNote(OpenDataBotShortNote):
    updatedTime = ""
    establishmentDate = ""
    director = ""
    managers = ""
    state = ""
    typeOfActivity = ""
    VATPayer = False
    