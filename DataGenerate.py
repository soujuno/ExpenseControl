# Um gerador aleatório de dados de despesas
# Quais dados? Data(aaaa-mm-dd)  
#              Descricao(ifood, gasolina,amazon, farmacia, suplementos, academia, mercado, padaria, netflix, spotify...)
#              valor(24.9, 30.00, 200.00, 19.9, 50.00, 123.00, 17.60, 83.50, 42.00, 55.50) 
#              transacao(pix,debito,credito)
#              receita(pix recebido do joao, salário, venda olx cadeira )
# Volumes de dados? Aproximadamente 200
# Período analisado? 06 meses

import csv      #Biblioteca para criar arquivos em formato de planilhas(.csv)
import random   #Esta biblioteca vai permitir a escolha aleatoria entre as despesas
from datetime import datetime, timedelta    #Estabelecer o período de coleta'
from time import sleep 
# --- Parâmetros ---
InitialDate = datetime(2026, 1, 1)
EndDate = datetime(2026, 6, 30)
Ano = 2026
#Lines = 200 #Alteração nas linhas

# --- Lista de variáveis --- 
Expenses = [
    ('iFood', 30, 80), ('GAS', 50, 140), ('Amazon', 25, 125), ('Growth', 135, 670),
    ('Pharm', 55, 123), ('Bakery', 11, 37), ('PetShop', 50, 100), ('After', 25, 125),
    ('Market', 250, 550), ('iFood', 30, 80), ('TwitchSubs', 35, 75), ('Net', 25, 125),
    ('HouseServices', 80, 200),
]

# --- Lista de fixos --- 
Subscriptions = [('Netflix', 10,'Credit'), ('Gym', 40,'Credit'), ('Spotify', 8.9,'Debit'), 
                 ('Appletv', 23,'Debit'), ('Claude', 35,'Credit'), ('YTpremium', 10,'Debit')
]

Payment = ['DEBIT', 'CREDIT', 'PIX']

def DataGenerateRandom(data):
    print('Iniciando geração de dados mês a mês...')
    sleep(1)   

    AllTransactions = []

    for month in range(1,7):                        #Janeiro a Junho
        print(f'--- Dados do mês {month:02d}/2026 ---')
        
        for Description, Price, Pay in Subscriptions:
            DateDays = random.randint(1, 28)            #Gera uma data aleatória entre 1 e 28
            DateTrans= datetime(2026, month, DateDays)  #Transforma em uma data de calendário, puxando o DateDays
            DateStr  = DateTrans.strftime('%Y-%m-%d')   #Transformar data em string

        NTrans = [DateStr, Description, Price, Pay]
        AllTransactions.append(NTrans)

        x = random.randint(25,35)
        for _ in range(x):
            DateDaysE = random.randint(1,28)
            DateTransE = datetime(Ano, month, DateDaysE)
            DateStrE  = DateTransE.strftime('%Y-%m-%d')

            DescriptionE, MinPrice, MaxPrice = random.choice(Expenses)
            PriceE = round(random.uniform(MinPrice, MaxPrice), 2)
            Transaction = random.choice(Payment)

            NTransE = [DateStrE, DescriptionE, f'{PriceE:.2f}', Transaction]
            AllTransactions.append(NTransE)

    print(f'\nTotal de {len(AllTransactions)} transações geradas.')
    print(f'Escrevendo dados no arquivo...')

        #Head csv
    Head = (['date', 'expenses', 'price', 'payment'])
    with open (data, mode = 'w', newline = '', encoding = 'utf-8') as archive_csv:
        writer_csv = csv.writer(archive_csv)
        writer_csv.writerow(Head)
        writer_csv.writerows(AllTransactions)

        print('Arquivo gerado com sucesso!')

# --- Creation ---
if __name__ == "__main__":
    DataGenerateRandom('DataBase.csv')

