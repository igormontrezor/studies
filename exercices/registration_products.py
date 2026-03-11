prod = {}
total = plus_thousd = 0
while True:
    name = input('Type the name of product: ')
    price = float(input(f'Type the price of {name}: '))
    prod.update({name: price})
    nw_product = int(input('Want to add new product?\n1 - Yes\n2 - No\n...'))
    if nw_product == 2:
        for p in prod.values():
            print(p)
            total += p
            if p > 1000:
                plus_thousd += 1
        break
prod = dict(sorted(prod.items(), key=lambda item: item[1]))
print(f'\nTotal: {total}\nProducts plus thousand: {plus_thousd}\nThe Plus is: {list(prod.items())[-1]}\nThe Lowest is: {list(prod.items())[0]}')