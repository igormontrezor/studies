import sys
import register
import show
import time



def initial():
    try:
        while True:
            option = int(
                input("1 - New Player\n2 - Players in System\n3 - Show Player Statistics\n4 - End System\n::: ")
            )
            if option == 1:
                while True:
                    quantity = 1
                    register.load_from_file()
                    name = input(f"\nEnter the name of {quantity}° player: ").title()
                    if name in [p['name'] for p in register.players]:
                        print(f'Player {name} already exists!')
                        continue
                    else:
                        matches = int(input("Enter the quantity of matches of this player: "))
                        register.user(name, matches)
                    add_player = input('Add one more player?\n(Exit to end): ').capitalize()
                    quantity += 1
                    if add_player == 'exit'.capitalize():
                        break
                    #show.print_statistics(register.players)
            elif option == 2:
                register.player.clear()
                register.load_from_file()
                show.print_statistics(register.players)
            elif option == 3:
                register.load_from_file()
                show.show_player_statistics(register.players)
            elif option == 4:
                print('Goodbye!')
                sys.exit()
    except ValueError:
        import time
        time.sleep(0.5)
        print('\nInvalid option!')
        time.sleep(0.5)
        print('Returning to main menu...\n')
        time.sleep(0.5)
        initial()


if __name__ == "__main__":
    initial()
