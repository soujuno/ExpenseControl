import csv
from time import sleep

#Title
sleep(0.5)
print('--------------------------------------------')
print(F'{"EXPENSES ANALYZER V.1.0":>32}')
print('--------------------------------------------')
sleep(1)

# abrir = 'DataBase.csv'

def load_expenses(archive_csv):
    print(f'  {"Reading File...":>26}  ')
    print('--------------------------------------------')
    sleep(1.5)
    with open(archive_csv, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)

        header = next(reader)

        header_without_date = header[1:]
        print(header_without_date)
        sleep(2)
        print('--------------------------------------------')

        selection = [1,2,3]

        for l in reader:
            dados = [l[i] for i in selection]
            print(f'{dados:>25}')
            print()

if __name__ == "__main__":
    load_expenses('DataBase.csv')


#processador.py = categorizar despesas → def categorizar → Criar dic com cada categoria 3 no max

