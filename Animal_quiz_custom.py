print('Welcome to my animal quiz!')

playing = input('Do you want to play? ')

if playing != 'yes':
    quit()

print('Okay! Here we go!')

answer = input('How many legs does a spider have? ')
if answer == '8':
    print('Correct! ')
else:
    print('Incorrect!')

answer = input('What do owls eat? ')
if answer == 'meat':
    print('Correct! ')
else:
    print('Incorrect!')

answer = input('What do you call a batch of lions? ')
if answer == 'pride':
    print('Correct! ')
else:
    print('Incorrect!')

answer = input('Do snakes shed their skin? ')
if answer == 'yes':
    print('Correct! ')
else:
    print('Incorrect!')

print('Thank you for playing!')
quit()
