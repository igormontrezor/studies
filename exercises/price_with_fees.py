product = float(input('What the price: '))
metod_pay = int(input('Type 1 for Money\nType 2 for CreditCard 1x\nType 3 for CreditCard 2x\nType 4 for CreditCard 3x\n'))
if metod_pay == 1:
    product -= (10/100)*product
    print(product)
elif metod_pay == 2:
    product -= (5/100)*product
    print(product)
elif metod_pay == 4:
    product += (20/100)*product
    print(product)
else:
    print(product)