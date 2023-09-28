# coding: cp1251
import OpenDataBotObject
import UakeyClient
import Client
#from bs4 import BeautifulSoup as BS
import csv

codes = []

# INPUT
#with open('db\\input\\1.html', 'r', encoding='cp1251') as inputDB:
#    contents = inputDB.read()
#    soup = BS(contents, 'html.parser')

#    soup = soup.find_all('td', class_='s0')
#    for el in soup:
#        codes.append(el.get_text())
#    codes = list(filter(None, codes))

#    # DEBUG
#    print('WE GOT INPUT\n')

with open('db\\input\\2.txt', 'r') as inputDB:
    for line in inputDB:
        codes.append(line.strip())

output_file_path = 'db\\output\\output.csv'

# Відкриваємо файл для запису, щоб очистити його
with open(output_file_path, 'w', newline='', encoding='utf-8') as clear_file:
    pass  # Записуємо нічого, тобто очищаємо файл

def add_company_to_csv(code, name, emails, phones, registered):
    with open(output_file_path, 'a', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Записуємо рядок заголовку, якщо файл порожній
        if csv_file.tell() == 0:
            csv_writer.writerow(['code', 'name', 'email', 'phones', 'registered'])

        phones_str = ', '.join(phones)
        emails_str = ', '.join(emails)
        row = [code, name, emails_str, phones_str, registered]
        csv_writer.writerow(row)
        csv_file.flush()  # Забезпечуємо негайний запис даних
        # DEBUG
        print('Компанію додано')

def add_problem_code(code):
    with open('db\\output\\problemCodes.txt', 'a+') as problem_file:
        problem_file.seek(0)  # Переміщуємо курсор на початок файлу для читання
        existing_codes = problem_file.read().splitlines()

        if code not in existing_codes:
            problem_file.write(code + '\n')

def save_potential_clients(codes):
    for one in codes:
        try:
            client_in_OpenDataBot = OpenDataBotObject.OpenDataBotShortNote(one)

            client_in_Uakey = UakeyClient.UakeyClient(one)

            client = Client.Client(client_in_Uakey, client_in_OpenDataBot)

            # DEBUG
            print(f'-----------{one}')


            print(one + '\t ' + str(client.registered))

            add_company_to_csv(
                client.code,
                client.name,
                client.emails,
                client.phones,
                client.registered
            )
        except Exception as e:
            print(f'-----------{one}')
            print(f'Помилка обробки компанії {one}: {str(e)}')
            add_company_to_csv(
                one,
                '',
                '',
                '',
                ''
            )
            add_problem_code(one)

    # DEBUG
    print('OUTPUT WAS COMPLETED')

# Викликаємо функцію save_potential_clients, яка додасть відповідні компанії до файлу
save_potential_clients(codes)

# DEBUG
print('\nFINISH')
