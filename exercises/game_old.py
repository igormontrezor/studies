import random

import time





def choice():

    try:

        player_choice = int(input("Enter whith 1 for X or 2 for O: "))

        pc_choice = ""

        if player_choice == 1:

            player_choice = "X"

            pc_choice = "O"

            return player_choice, pc_choice

        elif player_choice == 2:

            player_choice = "O"

            pc_choice = "X"

            return player_choice, pc_choice

        else:

            print("Invalid choice")

            choice()

    except:

        print("Invalid choice")

        choice()





def play_game(the_board, choice, pc_choice):

    print(choice, pc_choice)

    while True:

        try:

            print_board(the_board)

            print(the_board)

            player_move = input('What your move? top-, mid-, low- (L, M, R): ')

            print(f'Player move: {player_move}')

            pc_move = random.choice(['top-L', 'top-M', 'top-R', 'mid-L', 'mid-M', 'mid-R', 'low-L', 'low-M', 'low-R'])

            print(f'PC move: {pc_move}')

            if the_board[player_move] == ' ' and the_board[pc_move] == ' ':

                the_board[player_move] = choice

                time.sleep(0.5)

                the_board[pc_move] = pc_choice

                time.sleep(0.5)

                print_board(the_board)

                winner()

            elif the_board[player_move] != ' ' or the_board[pc_move] != ' ':

                print('Invalid move')

                play_game(the_board, choice, pc_choice)

        except:

            print('Invalid move')

            play_game(the_board, choice, pc_choice)



def winner():

    if the_board['top-L'] == choice and the_board['top-M'] == choice and the_board['top-R'] == choice:

        print('Player wins!')

        return True

    elif the_board['mid-L'] == choice and the_board['mid-M'] == choice and the_board['mid-R'] == choice:

        print('Player wins!')

        return True

    elif the_board['low-L'] == choice and the_board['low-M'] == choice and the_board['low-R'] == choice:

        print('Player wins!')

        return True

    elif the_board['top-L'] == choice and the_board['mid-L'] == choice and the_board['low-L'] == choice:

        print('Player wins!')

        return True

    elif the_board['top-M'] == choice and the_board['mid-M'] == choice and the_board['low-M'] == choice:

        print('Player wins!')

        return True

    elif the_board['top-R'] == choice and the_board['mid-R'] == choice and the_board['low-R'] == choice:

        print('Player wins!')

        return True

    elif the_board['top-L'] == choice and the_board['mid-M'] == choice and the_board['low-R'] == choice:

        print('Player wins!')

        return True

    elif the_board['top-R'] == choice and the_board['mid-M'] == choice and the_board['low-L'] == choice:

        print('Player wins!')

        return True

    elif the_board['top-L'] == pc_choice and the_board['top-M'] == pc_choice and the_board['top-R'] == pc_choice:

        print('PC wins!')

        return True

    elif the_board['mid-L'] == pc_choice and the_board['mid-M'] == pc_choice and the_board['mid-R'] == pc_choice:

        print('PC wins!')

        return True

    elif the_board['low-L'] == pc_choice and the_board['low-M'] == pc_choice and the_board['low-R'] == pc_choice:

        print('PC wins!')

        return True

    elif the_board['top-L'] == pc_choice and the_board['mid-L'] == pc_choice and the_board['low-L'] == pc_choice:

        print('PC wins!')

        return True

    elif the_board['top-M'] == pc_choice and the_board['mid-M'] == pc_choice and the_board['low-M'] == pc_choice:

        print('PC wins!')

        return True

    elif the_board['top-R'] == pc_choice and the_board['mid-R'] == pc_choice and the_board['low-R'] == pc_choice:

        print('PC wins!')

        return True

    elif the_board['top-L'] == pc_choice and the_board['mid-M'] == pc_choice and the_board['low-R'] == pc_choice:

        print('PC wins!')

        return True

    elif the_board['top-R'] == pc_choice and the_board['mid-M'] == pc_choice and the_board['low-L'] == pc_choice:

        print('PC wins!')

        return True

    else:

        print('Draw!')

    return False





def print_board(board):

    print(board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])

    print("-+-+-")

    print(board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])

    print("-+-+-")

    print(board["low-L"] + "|" + board["low-M"] + "|" + board["low-R"])





the_board = {

    "top-L": " ",

    "top-M": " ",

    "top-R": " ",

    "mid-L": " ",

    "mid-M": " ",

    "mid-R": " ",

    "low-L": " ",

    "low-M": " ",

    "low-R": " ",

}



player_choice, pc_choice = choice()

play_game(the_board, player_choice, pc_choice)
