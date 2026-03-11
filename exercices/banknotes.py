banknotes = (1, 10, 20, 50, 100)
total = []
money = int(input('What amount do you want withdraw?\n'))
while  money != 0:
    #for notes in banknotes:
    if money >= banknotes[0] and money < banknotes[1]:
           money -= banknotes[0]
           total.append(banknotes[0])
    if money >= banknotes[1] and money < banknotes[2]:
            money -= banknotes[1]
            total.append(banknotes[1])
    if money >= banknotes[2] and money < banknotes[3]:
            money -= banknotes[2]
            total.append(banknotes[2])
    if money >= banknotes[3] and money < banknotes[4]:
           money -= banknotes[3]
           total.append(banknotes[3])
    if money >= banknotes[4]:   
           money -= banknotes[4]
           total.append(banknotes[4])
for note in total:
       print(f'Saída: {note}')
print(f'Total: {sum(total)}')