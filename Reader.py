import csv
from time import sleep
sleep(0.5)
print('--------------------------------------------')
print(F'{"EXPENSES ANALYZER V.1.0":>32}')
print('--------------------------------------------')
sleep(1)

abrir = 'DataBase.csv'

# def load_expenses(data):
print(f'  {"Reading File...":>26}  ')
print('--------------------------------------------')
sleep(1.5)
with open(abrir, 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)

    header = next(reader)

    header_without_date = header[1:]
    print(header_without_date)
    sleep(2)
    print('--------------------------------------------')

    selection = [1,2,3]

    for l in reader:
        dados = [l[i] for i in selection]

        # print(l)
        print(dados)
        print()

#def
#processador.py = categorizar despesas → def categorizar → Criar dic com cada categoria 3 no max

