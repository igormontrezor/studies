t1 = int(input('Type the fisrt straight: '))
t2 = int(input('Type the second straight: '))
t3 = int(input('Type the third straight: '))

if (t1+t2) > t3 and (t1+t3) > t2 and (t2+t3) > t1:
    print(f'Its a triangle!')
    if (t1 == t2) and (t1 == t3):
        print('Equilateral')
    elif (t1 == t2)  or (t1 == t3) or (t2 == t3):
        print('Isosceles')
    else:
        print('All diffent sides.')
else:
    print(f'Not a triangle!')