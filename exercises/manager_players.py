def register(name, matches):
    player['name'] = name
    player['matches'] = matches


def man_goals(matches):
    for m in range(matches):
        qt_goals.append(int(input(f'Type the quantity of goals {m+1} matche: ')))
    player['goals'] = qt_goals.copy()
    if player['matches'] > 0:
        player['goal_average'] = float(sum(qt_goals)/player['matches'])
    else:
        player['goal_average'] = 0
    player['total_goals'] = int(sum(qt_goals))
    players.append(player.copy())
    qt_goals.clear()

def print_statistics(players):
    while True:
        try:
            contn = input('Type continue C/B break: ').title()
            if contn == 'B':
                no, no_id, name_w, total_goals = 0, 4, 12, 4
                header = f'{'No':<{no_id}} | {'Name':<{name_w}} | {'Total Goals':<{total_goals}}'
                print(header)
                print('-' * len(header))
                for pls in players:
                    print(f'{no:<{no_id}} | {pls['name']:<{name_w}} | {pls['total_goals']:<{total_goals}}')
                    no += 1
                print('-' * len(header))
                break
            else:
                print('======================================')
                print('Players in system:\n')
            for name in players:
                print(name['name'])
            print('======================================')
            namep = input('Name: ').title()
            for dat in players:
                if namep == dat['name']:
                    print(f'--Statistics: {namep}')
                    for n, g in enumerate(dat['goals']):
                        print(f'{n+1}° - Game goals score {g}.')
                    print(f'Total Matches: {dat['matches']}\nTotal Goals: {dat['total_goals']}')      
        except print: 
            print(f'\n===Error {contn}! this player not exist.===\n')


player = dict()
qt_goals = list()
players = list()
try:
    quantity = int(input('Type the quantity manager player: '))
except:
    quantity = 1
for q in range(quantity):
    name=input(f'Type the name of {q+1} player: ').title()
    if name == '':
        name = '<unknow>'.title()
    matches=int(input('Type the quantity of matches of this player: '))
    register(name, matches)
    man_goals(matches)
print_statistics(players)