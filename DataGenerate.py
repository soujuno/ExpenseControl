import csv      
import random   
from datetime import datetime    
from time import sleep 

# --- Parâmetros ---
Initial_Date = datetime(2026, 1, 1)
End_Date = datetime(2026, 6, 30)
Year = 2026
#Lines = 200 #Alteração nas linhas -- (Alterar)

# --- Lista de variáveis --- 
EXPENSES = [
    ('iFood', 30, 80), ('GAS', 50, 140), ('Amazon', 25, 125), ('Growth', 135, 670),
    ('Pharm', 55, 123), ('Bakery', 11, 37), ('PetShop', 50, 100), ('After', 25, 125),
    ('Market', 250, 550), ('Bar', 30, 80), ('TwitchSubs', 35, 75), ('Net', 25, 125),
    ('HouseServices', 80, 200),
]

# --- Lista de fixos --- 
SUBSCRIPTIONS = [('Netflix', 10,'Credit'), ('Gym', 40,'Credit'), ('Spotify', 8.9,'Debit'), 
                 ('Appletv', 23,'Debit'), ('Claude', 35,'Credit'), ('YTpremium', 10,'Debit')
]

Payment = ['DEBIT', 'CREDIT', 'PIX']

def DataGenerateRandom(Data):
    print('Iniciando geração de dados mês a mês...')
    sleep(1)   

    All_Transactions = []

    for month in range(1,7):                        #Janeiro a Junho
        print(f'--- Dados do mês {month:02d}/2026 ---')
        
        for Description, Price, Pay in SUBSCRIPTIONS:
            Date_Days = random.randint(1, 28)            
            Date_Trans= datetime(2026, month, Date_Days)  
            Date_Str  = Date_Trans.strftime('%Y-%m-%d')   

        New_Trans = [Date_Str, Description, Price, Pay]
        All_Transactions.append(New_Trans)

        x = random.randint(25,35)
        for _ in range(x):
            Date_Days_Expenses = random.randint(1,28)
            Date_Trans_Expenses = datetime(Year, month, Date_Days_Expenses)
            Date_Str_Expenses  = Date_Trans_Expenses.strftime('%Y-%m-%d')

            Description_Expenses, Min_Price, Max_Price = random.choice(EXPENSES)
            Price_Expenses = round(random.uniform(Min_Price, Max_Price), 2)
            Transaction = random.choice(Payment)

            New_Trans_Expenses = [Date_Str_Expenses, Description_Expenses, f'{Price_Expenses:.2f}', Transaction]
            All_Transactions.append(New_Trans_Expenses)

    print(f'\nTotal de {len(All_Transactions)} transações geradas.')
    print(f'Escrevendo dados no arquivo...')

        #Head csv
    Head = (['date', 'expenses', 'price', 'payment'])
    with open (Data, mode = 'w', newline = '', encoding = 'utf-8') as archive_csv:
        writer_csv = csv.writer(archive_csv)
        writer_csv.writerow(Head)
        writer_csv.writerows(All_Transactions)

        print('Arquivo gerado com sucesso!')

# --- Creation ---
if __name__ == "__main__":
    DataGenerateRandom('DataBase.csv')

