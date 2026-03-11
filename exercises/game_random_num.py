import random

print('Game guess the number')
name = input('Enter your name: ')
number_drawn = random.randint(1,10)
count = 0
print(f'Hello {name}! Guess the number between 1 and 10')

def game_guess(number_drawn):
    while True:
        number = int(input('Enter a number'))
        if number == number_drawn:
            print(f"You Win {name}! The number was {result}")
            return number_drawn
        elif number > number_drawn:
            print('Too high')
        else:
            print('Too low')
        if count == 6:
            print('You lose!')
            break
        count += 1

result = game_guess(number_drawn)
print(f'the number was {result}')
