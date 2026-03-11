import time


def info_help():
    name_fuction = str()
    while name_fuction != 'End':
        time.sleep(0.5)
        print(f'{"~"*14}\nSYSTEM PyHELP\n{"~"*14}')
        name_fuction = input('Enter whit function name: ')
        try:
            print(f'Acessing {name_fuction} manual...')
            time.sleep(0.7)
            print(help(name_fuction))
        except name_fuction:
            print('Error, this function not exist.')
    print(f'{"~"*14}\nBye Bye.\n{"~"*14}')
    print()
info_help()