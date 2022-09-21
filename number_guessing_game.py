from ast import Break
import random

top_of_range = input('Type a number: ')

if top_of_range.isdigit():
    tor_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time. ')
        quit()
else:
    print('Please type a number larger than 0 next time. ')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
else:
    print('Please type a number larger than 0 next time. ')
    

if user_guess == random_number:
    print('You got it correct! ')
    Break
else:
    print('Try to guess again. ')
