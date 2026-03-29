import main
import time


def print_statistics(players):
    while True:
        if len(players) != 0:
            no, no_id, name_w, total_goals = 1, 4, 15, 4
            time.sleep(1)
            print('-' * 40)
            header = f'{'No':<{no_id}} | {'Name':<{name_w}} | {'Total Goals':<{total_goals}}'
            print(header)
            for pls in players:
                print(f'{no:<{no_id}} | {pls['name']:<{name_w}} | {pls['total_goals']:<{total_goals}}')
                no += 1
            print('-' * 40)
            players.clear()
            time.sleep(1)
            break

def show_player_statistics(players):
    while True:
        if len(players) != 0:
            namep = input('Name (exit to back): ').title()
            if namep == 'Exit':
                print('\nBack to main menu...\n')
                time.sleep(1)
                #players.clear()
                main.initial()
                break
            elif namep not in [p['name'] for p in players]:
                print('Analising...')
                time.sleep(0.5)
                print(f'{namep} do not exist, try again.')
                #players.clear()
                time.sleep(0.5)
            else:
                print(f'--Statistics: {namep}')
                for p in players:
                    for n, g in enumerate(p['goals']):
                        if p['name'] == namep:
                            time.sleep(0.5)
                            print(f'{n+1}° - Game goals score {g}.')
                        if n >= len(p['goals']):
                            break
                time.sleep(0.5)
                print('-' * 40)
                players.clear()
        break
def no_player_found():
    print('\nAnalysing...')
    time.sleep(0.5)
    print('No have players in database.\n')
    time.sleep(0.5)
    main.initial()