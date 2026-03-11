from treatment import show

def correction(num, percentage_upper, percentage_decrease):
    while True:
        try:
            num = float(num.replace(',', '.'))
            percentage_upper = float(input('Enter whith percentage upper: '))
            percentage_decrease = float(input('Enter whith percentage decrease: '))
            show.treatment(num, percentage_upper, percentage_decrease)
            break
        except:
            print(f'Error!\nIt has parameters which are not a number\n')
            num = input('Enter whith coin value: $')
            continue