# coding: cp1251
import OpenDataBotAPIviaParse
from bs4 import BeautifulSoup as BS
import csv

codes = []

# INPUT
with open('db\\input\\1.html', 'r', encoding='cp1251') as htmlDB:
    contents = htmlDB.read()
    soup = BS(contents, 'html.parser')

    soup = soup.find_all('td', class_='s4', limit=50)
    for el in soup:
        codes.append(el.get_text())
    codes = list(filter(None, codes))

    # DEBUG
    print('WE GOT INPUT\n')

output_file_path = 'db\\output\\output.csv'

# ³�������� ���� ��� ������, ��� �������� ����
with open(output_file_path, 'w', newline='', encoding='utf-8') as clear_file:
    pass  # �������� �����, ����� ������� ����

def add_company_to_csv(code, name, email, phones, address):
    with open(output_file_path, 'a', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)

        # �������� ����� ���������, ���� ���� �������
        if csv_file.tell() == 0:
            csv_writer.writerow(['code', 'name', 'email', 'phones', 'address'])

        phones_str = ', '.join(phones)
        row = [code, name, email, phones_str, address]
        csv_writer.writerow(row)
        csv_file.flush()  # ����������� �������� ����� �����
        # DEBUG
        print('������� ������')

def add_problem_code(code):
    with open('db\\output\\problemCodes.txt', 'a+') as problem_file:
        problem_file.seek(0)  # ��������� ������ �� ������� ����� ��� �������
        existing_codes = problem_file.read().splitlines()

        if code not in existing_codes:
            problem_file.write(code + '\n')

def save_potential_clients(codes):
    for one in codes:
        try:
            test_company = OpenDataBotAPIviaParse.OpenDataBotShortNote(one)
            # DEBUG
            print(f'-----------{test_company.code}')

            if "���" in test_company.address or "�������" in test_company.address:
                if test_company.registered:
                    print(test_company.code + '\t is ' + str(test_company.registered))

                    # �������� �������� ����� ����� �������
                    if test_company.name and test_company.email and test_company.phones and test_company.address:
                        add_company_to_csv(
                            test_company.code,
                            test_company.name,
                            test_company.email,
                            test_company.phones,
                            test_company.address
                        )
        except Exception as e:
            print(f'������� ������� ������ {one}: {str(e)}')
            add_problem_code(one)

    # DEBUG
    print('OUTPUT WAS COMPLETED')

# ��������� ������� save_potential_clients, ��� ������� ������� ������ �� �����
save_potential_clients(codes)

# DEBUG
print('\nFINISH')
