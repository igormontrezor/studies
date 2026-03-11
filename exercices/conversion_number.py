num = int(input('Type the number: '))
choice = int(input('Type for BIN(1), OCT(2), hexa(3): '))
bin = []
oct = []
hexa = []
if choice == int(1):
    while num // int(2):
        print(f'aqui{num}')
        bin.append(num%2)
        num = num // 2
        if num <= 0:
            break
    bin.append(num)
    bin = bin[::-1]
    print(bin)
if choice == int(2):
    while num // int(8):
        oct.append(num%8)
        num = num // 8
        if num <= 0:
            break
    oct.append(num)
    oct = oct[::-1]
    print(oct)
if choice == int(3):
    num = hex(num)
    hexa.append(num)
    '''if num == 13:
        hexa.append('= D')
    while num // int(16):
        hexa.append(num%16)
        if num%16 == 13:
            hexa.pop()
            hexa.append(str('D'))
        print(num%16)
        num = num // 16
        print(num)
        if num <= 0:
            break'''
    print(hexa)