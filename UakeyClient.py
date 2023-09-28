# coding: cp1251
import Parser

class UakeyClient():
    name = ''

    def __init__(self, code):
        code = str(code)
        while (len(code) < 8):
            code = '0' + code
        self.code = code
        url = 'https://cert.suzs.info/ru/BestzvitpaysSert/page.htm?edrpo='+ code + '&Bestzvitpaysid=3490051&acsk=2'  # URL сторінки
        page = Parser.soup(url)
        if(page is not None):
            if len(code) == 8:
                table = page.find_all('table', {'border': '0'})[3]
                
                rows = table.find_all('tr')
                
                for row in rows:
                    cells = row.find_all('td')
                    for cell in cells:
                        if "Ключ печатки" in cell.get_text():
                            self.name = cells[0].get_text()
                            break

            if len(code) == 10:
                table = page.find_all('table', {'border': '0'})[3]
                
                rows = table.find_all('tr')
                
                for row in rows:
                    cells = row.find_all('td')
                    for cell in cells:
                        cell_text = cell.get_text()
                        if "Ключ керівника" in cell_text or "Ключ директора" in cell_text:
                            self.name = cells[0].get_text()
                            break


            # Знайдіть всі тексти в стовпці "E-mail:" з вказаним класом
            parsed_emails = [email.get_text() for email in page.find_all('td', class_='flag2') if '@' in email.get_text()]
    
            # Видаліть дублікати
            self.emails = list(set(parsed_emails))

            print(f'\n {self.name}')

