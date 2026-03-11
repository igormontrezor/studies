weight = int(input('How many people: '))
total_weigth = []
ok = []
for p in range(weight):
    people = int((input(f'Wheight {p+1}: ')))
    total_weigth.append(people)
total_weigth.sort()
ok.append(total_weigth[0])
ok.append(total_weigth[weight-1])
print(f'The Lowest Weigth is: {ok[0]}\nThe Highest Weigth is: {ok[1]}')