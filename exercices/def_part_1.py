import random
import time


'''def area(width, height):
    print(f'The area of this place ({width}x{height}) is: ({float(width*height)}m²)')

w = float(input('Type the width: '))
h = float(input('Type the height: '))
area(w, h)'''

'''def print_txt(txt):
    size = len(txt)
    print(f'{"-" * size}')
    print(txt)
    print(f'{"-" * size}\n')

txt = ('Hello, World!')
print_txt(txt)'''

'''def cont(start, end, step):
    for n in range(start, end, step):
        print(n, end=' ')
        time.sleep(0.2)
    print(f'\n{'-'*(end)}')
    step = -2
    end = 10
    start = -1
    for n in range(end, start, step):
        print(n, end=' ')
        time.sleep(0.2)
    print(f'\n{'-'*(end)}')
    start = (int(input('Type the start: ')))
    end = (int(input('Type the end: ')))
    step = (int(input('Type the step: ')))
    if start > end and step > 0:
        end -= 1
        step = -(step)
        print(step)
    elif start > end and step < 0:
        step = step
    elif start < end and step > 0:
        step = step
    elif step == 0 and start < end:
        step = +1
    elif step == 0 and start > end:
        step = -1
    else:
        start , end = end, start
    for n in range(start, end, step):
        print(n, end=' ')
        time.sleep(0.2)
    
cont(0, 11, 1)'''

'''def high(*num):
    for n in num:
        inverse = (sorted(n,reverse=True))
        for d in n:
            print(d, end=' ')
            time.sleep(0.5)
    print(f'\n{'~'*len(num[0])}')
    print(f'The values infomed are: {n}\nWith {len(n)} numbers in total.\nThe bigger number is: {inverse[0]}')

linum = list()
counter = 0
while True:
    counter += 1
    loop = (int(input(f'Type the {counter}° (999 BREAK): ')))
    if loop == 999:
        break
    linum.append(loop)
    
high(linum)'''


def sort_num(num):
    """_summary_

    Args:
        num (_type_): _description_

    Returns:
        _type_: _description_
    """
    print(f'\n{"~"*35}')
    for n in range(0,5):
        num.append(random.randint(0,10))
    for n in num:
        print(n, end=' ')
        time.sleep(0.5)
    return num


def sum_num(num):
    """_summary_

    Args:
        num (_type_): _description_

    Returns:
        _type_: _description_
    """
    num = sort_num(num)
    sum_num = 0
    for n in num:
        if n%2 == 0:
            sum_num += n
    print(f'\nThe sum of pairs number are: {sum_num}')
    print(f'{"~"*35}')
    return sum_num

num=list()
result = sum_num(num)
print(result + 10)
print(num)
    