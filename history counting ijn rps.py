import random
turns = ['rock', 'paper', 'scissors']
human_turns = []
computer_turns = []
win_history = []


while(True):
    human_turn = input("Enter your turn, or type exit: ")
    computer_turn = random.choice(turns)

    human_turns.append(human_turn)
    computer_turns.append(computer_turn)

    if human_turn == 'exit':
        print('Thank you for playing! Bye bye')
        break
    
    print(f'Human:{human_turn} vs. Computer:{computer_turn}')
if human_turn == computer_turn:
    print('Draw!')
    win_history.append('draw')
elif human_turn == 'rock' and computer_turn == 'scissors':
    print('Human wins!')
    win_history.append('human wins')
elif human_turn == 'paper' and computer_turn == 'rock':
    print('Human wins!')
    win_history.append('human wins')
elif human_turn == 'scissors' and computer_turn == 'paper':
    print('Human wins!')
    win_history.append('human wins')
else:
    print('Computer wins!')
    win_history.append('human wins')

print(f'You have played {len(human_turns)} times')
print(human_turns)
print(computer_turns)
history = input("Do you want t see the game history? : ")
if history == 'yes':
    print(win_history)
