def upper(num,percentage_upper):
    num += (num*percentage_upper)/100
    return f'{num:.2f}'.replace('.', ',')

def decrease(num,percentage_decrease):
    num -= (num*percentage_decrease)/100
    return f'{num:.2f}'.replace('.', ',')

def double(num):
    num *= 2
    return f'{num:.2f}'.replace('.', ',')

def half(num):
    num = (num/2)
    return f'{num:.2f}'.replace('.', ',')