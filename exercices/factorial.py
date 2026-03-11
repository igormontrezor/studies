number = int(input('Type the number: '))
fact = 1
while 0 in range(number):
    print(number)
    fact *= number
    number -= 1
print(f'The factorial is !{fact}.')