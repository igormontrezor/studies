from treatment import count
def treatment(num, percentage_upper, percentage_decrease):
    show_num = (f'{num}')
    show_upper = (f'{count.upper(num, percentage_upper)} + {percentage_upper}%')
    show_decrease = (f'{count.decrease(num, percentage_decrease)} - {percentage_decrease}%')
    show_double = (f'{count.double(num)}')
    show_half = (f'{count.half(num)}')
    print('\n')
    no, upper, decrease, double, half = len(show_num), len(show_upper), len(show_decrease), len(show_double), len(show_half)
    header = (f'{'No':<{no}} | {'Upper':<{upper}} | {'Decrease':<{decrease}} | {'Double':<{double}} | {'Half':<{half}}')
    print(header)
    print(f'{num} | {show_upper} | {show_decrease} | {show_double} | {show_half}')
    print('~'*len(header))
