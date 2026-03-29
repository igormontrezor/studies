import time

player = dict()
qt_goals, players = list(), list()
def user(name, matches):
    players.clear()
    player['name'] = name
    player['matches'] = matches
    man_goals(matches)

def man_goals(matches):
    for m in range(matches):
        qt_goals.append(int(input(f'Enter the quantity of goals {m+1} matche: ')))
    player['goals'] = qt_goals.copy()
    if player['matches'] > 0:
        player['goal_average'] = float(sum(qt_goals)/player['matches'])
    else:
        player['goal_average'] = 0
    player['total_goals'] = int(sum(qt_goals))
    save_to_file(player)
    time.sleep(0.5)
    print(f'\nPlayer {player["name"]} registered successfully.')
    time.sleep(0.5)
    qt_goals.clear()

def save_to_file(player, filename="manager_players/players_data.txt"):
    with open(filename, 'a', encoding='utf-8') as file:
        goals_str = ','.join(map(str, player['goals']))
        line = f"{player['name']};{player['matches']};{goals_str};{player['goal_average']};{player['total_goals']}\n"
        file.write(line)

def load_from_file(filename="manager_players/players_data.txt"):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():
                    data = line.strip().split(';')
                    player = {
                        'name': data[0],
                        'matches': int(data[1]),
                        'goals': list(map(int, data[2].split(','))),
                        'goal_average': float(data[3]),
                        'total_goals': int(data[4])
                    }
                    players.append(player)
            file.close()
        

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")