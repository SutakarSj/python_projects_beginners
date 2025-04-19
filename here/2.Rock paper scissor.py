#Rock,Paper,Scissor game
import random

option=("stone","paper","scissor")
running=True
player_score=0
computer_score=0

while running:
    computer=random.choice(option)
    player=None 
    
    while player not in option:
        player=input("Enter ur option (Stone, Paper, Scissor):")
    print(f"\nPlayer = {player}")
    print(f"Computer = {computer}")
    
    if player=="scissor" and computer=="paper" or player=="stone" and computer=="scissor" or player=="paper" and computer=="stone":
        player_score+=1
    
    if player=="paper" and computer=="scissor" or player=="scissor" and computer=="stone" or player=="stone" and computer=="paper":
        computer_score+=1    
   
    if player==computer:
        continue
            
    your_choice = input("\nif continue yes or-else no :")
    if your_choice=="no" or your_choice!="yes":
        running=False

if player_score > computer_score:
    print(f"\nPlayer Score = {player_score}")
    print(f"Computer Score = {computer_score}")
    print("\n***YOU WIN***")
    
elif player_score < computer_score:
    print(f"\nPlayer Score = {player_score}")
    print(f"Computer Score = {computer_score}")
    print("\n***YOU LOSS***")
    
elif player_score==computer_score:
    print(f"\nPlayer Score = {player_score}")
    print(f"Computer Score = {computer_score}")
    print("\n***MATCH TIE***")
    
print("\nThank you for playing")