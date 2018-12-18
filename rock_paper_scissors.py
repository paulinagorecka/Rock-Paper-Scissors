""" 
Rock, Paper, Scissors is a classic tie-braking game. Enjoy!
"""

from random import randint

options = ["ROCK", "PAPER", "SCISSORS"]
message = {
  "tie": "Yawn.. It's a tie.",
  "won": "Yay! You won!",
  "lost": "Aww.. You lost!"
}

def decide_winner(user_choice, computer_choice):
  print "You picked: %s" % (user_choice)
  print "I picked: %s" % (computer_choice)
  if user_choice == computer_choice:
    print message["tie"]  
  elif user_choice == options[0] and computer_choice == options[2]:
    print message["won"]
  elif user_choice == options[1] and computer_choice == options[0]:
    print message["won"]
  elif user_choice == options[2] and computer_choice == options[1]:
    print message["won"]
  else:
    print message["lost"]
  
def play_RPS():
  user_choice = raw_input("Select Rock, Paper, or Scissors: ").upper()
  computer_choice = options[randint(0, 2)]
  decide_winner(user_choice, computer_choice)

play_RPS()
  
  
    
  
    
  

