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

#Parâmetros
InitialDate = datetime(2026, 1, 1)
EndDate = datetime(2026, 6, 30)
Lines = 200


Expenses = [
    ('iFood', 30, 80), ('GAS', 50, 140), ('Amazon', 25, 125), ('Growth', 135, 670),
    ('Pharm', 55, 123), ('Bakery', 11, 37), ('PetShop', 50, 100), ('After', 25, 125),
    ('Market', 250, 550), ('iFood', 30, 80), ('TwitchSubs', 35, 75), ('Net', 25, 125),
    ('Amazon', 25, 125),
]

## Lista de fixos = Netflix, gym, spotify, appletv, claude, ytpremium
Subscriptions = [('Netflix')]

Payment = ['DEBIT', 'CREDIT', 'PIX']

#                       ------- Principal -------
def DataGenerateRandom(data):
    print(f'Gerando {Lines} linhas de dados de consumo do Superman...')
    with open (data, mode = 'w', newline = '', encoding = 'utf-8') as archive_csv:
        writer_csv = csv.writer(archive_csv)


        # Head csv
        writer_csv.writerow(['date', 'expenses', 'price', 'payment'])

        # Lines CSV
        for _ in range(Lines):
            # Random Dates
            DateDays = (EndDate - InitialDate).days
            DateRand = InitialDate + timedelta(days=random.randrange(DateDays))
            DateStr  = DateRand.strftime('%Y-%m-%d')

            # Choose expenses and price
            Description, MinPrice, MaxPrice = random.choice(Expenses)
            price = round(random.uniform(MinPrice, MaxPrice), 2)

            # Transaction 
            Transaction = random.choice(Payment)

            writer_csv.writerow([DateStr, Description, price, Transaction])

    # Confirmation
    print(f'Arquivo {data} criado com sucesso!')

# --- Creation ---
if __name__ == "__main__":
    DataGenerateRandom('DataBase.csv')