shopping_list = {'piekarnia': ['chleb', 'paczek', 'bulka'],
                'warzywniak': ['marchew', 'seler', 'rukola'],
                'drogeria': ['szampon', 'krem']}

for shop, list in shopping_list.items():
    print(f"Ide do {shop.capitalize()} i kupuje {[l.capitalize() for l in list]}")