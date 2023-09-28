# coding: cp1251
import Parser

class UakeyClient():
    name = ''

    def __init__(self, code):
        code = str(code)
        while (len(code) < 8):
            code = '0' + code
        self.code = code
        url = 'https://cert.suzs.info/ru/BestzvitpaysSert/page.htm?edrpo='+ code + '&Bestzvitpaysid=3490051&acsk=2'  # URL �������
        page = Parser.soup(url)
        if(page is not None):
            if len(code) == 8:
                table = page.find_all('table', {'border': '0'})[3]
                
                rows = table.find_all('tr')
                
                for row in rows:
                    cells = row.find_all('td')
                    for cell in cells:
                        if "���� �������" in cell.get_text():
                            self.name = cells[0].get_text()
                            break

            if len(code) == 10:
                table = page.find_all('table', {'border': '0'})[3]
                
                rows = table.find_all('tr')
                
                for row in rows:
                    cells = row.find_all('td')
                    for cell in cells:
                        cell_text = cell.get_text()
                        if "���� ��������" in cell_text or "���� ���������" in cell_text:
                            self.name = cells[0].get_text()
                            break


            # ������� �� ������ � ������� "E-mail:" � �������� ������
            parsed_emails = [email.get_text() for email in page.find_all('td', class_='flag2') if '@' in email.get_text()]
    
            # ������� ��������
            self.emails = list(set(parsed_emails))

            print(f'\n {self.name}')

