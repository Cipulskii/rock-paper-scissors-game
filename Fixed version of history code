import random
turns = ['rock', 'paper', 'scissors']
human_turns = []
computer_turns = []
win_history = []

while(True):
    human_turn = input('Enter your turn, or type exit:')
    computer_turn = random.choice(turns)

    human_turns.append(human_turn)
    computer_turns.append(computer_turn)

    print(f'Human:{human_turn} vs. computer: {computer_turn}')
    if human_turn == computer_turn:
        if human_turn == 'exit':
            break
        print('Draw!')
        win_history.apend('Draw')
    elif human_turn == 'rock' and computer_turn == 'scissors':
        print('Human wins!')
        win_history.apend('Human wins!')
    elif human_turn == 'paper' and computer_turn == 'rock':
        print('Human wins!')
        win_history.apend('Human wins!')
    elif human_turn == 'scissors' and computer_turn == 'paper':
        print('Human wins!')
        win_history.apend('Human wins!')
    else:
        print('Computer wins!')
        win_history.apend('Computer wins!')
       

    print(f'You have played {len(human_turns)} times')
    print(human_turns)
    print(computer_turns)
    print('win_history')
