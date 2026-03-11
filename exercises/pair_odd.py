n1 = int(input('Insert the firt number: '))
n2 = int(input('Insert the second number: '))
pair = []
odd = []
multt = []
for n in range (n1, n2+1) or range (n2, n1+1):
    if n%2 == 0:
        pair.append(n)
    if n%3 == 0:
        multt.append(n)
    if n%2 == 1:
        odd.append(n)

print(f'Pair: {pair}\nOdd: {odd}')
print(f'Sum Pair: {sum(pair)}')
print(f'Sum Odd: {sum(odd)}')
print(f'Sum Multiple of 3: {sum(multt)}')