from reader import load_expenses
from handler import category, calculate

def analysis(total):
    print(F'{"EXPENSES ANALYZER V.1.0":>32}')
    if not total:
        print('No expenses!')
        return
    
    for category, end in total.items():
        print(f'- {category}: $ {end:.2f}')

    print('-------------------------------------')

def main():

    name_archive = 'DataBase.csv'

    read = load_expenses(name_archive)

    if not read:
        print('Finishing Program...')
        return
    
    for description in read:
        category(description)

    all_category = calculate(read)
    analysis(all_category)

if __name__ == '__main__':
    main()