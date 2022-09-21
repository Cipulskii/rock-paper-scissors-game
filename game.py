print('Welcome to my computer quiz!')

playing = input('Do you want to play? ')

if playing != 'yes':
    quit()

print('Okay! Here we go!')

answer = input('What does CPU stand for? ')
if answer == 'central processing unit':
    print('Correct! ')
