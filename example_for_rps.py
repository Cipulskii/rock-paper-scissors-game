import random
player1 = input("Player 1, please enter your name: ")
def script():
  print("Please, choose one of three: rock, paper, scissors")
  player1_figure = input(player1 + ", " + "enter your figure: ")
  figure = ["paper", "rock", "scissors"]
  computer_figure = random.choice(figure)
  print(f'Human: {player1_figure} vs. Computer: {computer_figure}')

  if player1_figure == computer_figure:
    print("Draw")
  
  elif player1_figure == "rock" and computer_figure == "scissors":
    print(player1 + ", you win")
  elif player1_figure == "scissors" and computer_figure == "paper":
    print(player1 + ", you win")
  elif player1_figure == "paper" and computer_figure == "rock":
    print(player1 + ", you win")
  else:
    print(player1 + ", you lose")
  
  restart = input("Would you like to play again? ")
  if restart == "yes" or restart == "y":
    script()
  if restart == "n" or restart == "no":
    print("Good bye!")
script()
