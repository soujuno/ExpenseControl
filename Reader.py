import csv
from time import sleep

    #Title
sleep(0.5)
print('--------------------------------------------')
print(F'{"EXPENSES ANALYZER V.1.0":>32}')
print('--------------------------------------------')
sleep(1)

    # Main -- Reader

def load_expenses(archive_csv='DataBase.csv'):
    print(f'  {"Reading File...":>26}  ')
    print('--------------------------------------------')
    sleep(1.5)

    dados = []

    with open(archive_csv, 'r', newline='', encoding='utf-8') as file:
    #Change to dict     
        reader = csv.DictReader(file)      
        for l in reader:
            dados.append(l)
    return dados

if __name__ == "__main__":
    load_expenses()

            

