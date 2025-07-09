def category(new_description):
    
    new_dict = new_description['expenses'].lower()

    if 'ifood' in new_dict or 'bakery' in new_dict or 'market' in new_dict:
        new_description['category'] = 'Food'
    elif 'gas' in new_dict:
        new_description['category'] = 'Transport'
    else:
        new_description['category'] = 'Others'

def calculate(description_new):
    all_expenses = {}

    for expense in description_new:
        name = expense['category']
        result = float(expense['price'])

        if name not in all_expenses:
            all_expenses[name] = 0.0

        all_expenses[name] += result

    return all_expenses