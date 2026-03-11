num = input('Type the number: ')
numint = int(num)
div = [int(ni) for ni in num]
thtu = []
thous = 0
hund = 0
ten = 0
uni = 0

for n in range(len(div)):
    if div[n] > 0:
        while numint > 999 and numint < 10000:
            numint = (numint - 1000)
            thous += 1
            
        while numint > 99 and numint < 1000:
            numint = (numint - 100)
            hund += 1
            
        while numint > 9 and numint < 100:
            numint = (numint - 10)
            ten += 1
            
        while numint > 0 and numint < 10:
            numint = (numint - 1)
            uni += 1
    #def 

thtu.append(thous)
thtu.append(hund)
thtu.append(ten)
thtu.append(uni)
    
print (thtu)
print (f'thousands: {thous}')
print (f'hundreds: {hund}')
print (f'tens: {ten}')
print (f'units: {uni}')