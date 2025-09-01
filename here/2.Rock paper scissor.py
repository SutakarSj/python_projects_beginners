#Rock,Paper,Scissor game
import random

option=("rock","paper","scissor")
running=True
player_score=0 #if the player wins the score will be incremented by 1
computer_score=0 #if the system wins the score will be incremented by 1

while running:
    computer=random.choice(option) #for selecting random value from the given choices
    player=None 
    
    while player not in option:
        player=input("Enter ur option (rock, Paper, Scissor):")
    print(f"\nPlayer = {player}")
    print(f"Computer = {computer}")
    
    if player=="scissor" and computer=="paper" or player=="rock" and computer=="scissor" or player=="paper" and computer=="rock": # Winning possibilities for the player
        player_score+=1
    
    if player=="paper" and computer=="scissor" or player=="scissor" and computer=="rock" or player=="rock" and computer=="paper": # Winning possibilities for the system
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
