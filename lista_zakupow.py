shopping_list = {'piekarnia': ['chleb', 'paczek', 'bulka'],
                'warzywniak': ['marchew', 'seler', 'rukola'],
                'drogeria': ['szampon', 'krem', 'chusteczki'],
                'meblowy': ['komoda', 'stolik']}

numb_prod = 0
for shop, list in shopping_list.items():
    print(f"Ide do {shop.capitalize()} i kupuje {[l.capitalize() for l in list]}")
    numb_prod += len(list)

print(f"W sumie kupuje {numb_prod} produktow.")

print("Pozdrowienia!!!")