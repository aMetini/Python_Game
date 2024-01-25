import random

choices = ["rock", "paper", "scissors"]

print("\nWelcome to the game: Rock, Paper, Scissors!\n")
print("Here are the rules of the game:")
print("""
    Rock wins over scissors
    Scissors wins over paper
    Paper wins over rock
    If both the computer and the player choose the same option, the result is a tie.")
""")

while True:
    user_play = input("Please select (rock, paper, scissors):").lower()


    if user_play not in choices:
        print("Invalid selection! Select (rock, paper, scissors)")
    else:
     print(f"You selected: {user_play}")
     break

computer_play = random.choice(choices)
print(f"The computer chose: {computer_play}")

if user_play == computer_play:
   print("It's a tie!") 
elif (
   (user_play == 'rock' and computer_play == 'scissors') or
   (user_play == 'paper' and computer_play == 'rock') or
   (user_play == 'scissors' and computer_play == 'paper')
):
   print("Player wins!") 
else:
   print("Computer wins!") 

print(f"\nWould you like to play again? Y/N")

   


