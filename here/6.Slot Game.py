#Slot Game 
import random

running = True

total_investment = 0

# Track how many coins the user has won
user_coin = 0

# Slot machine reels with symbols
option1 = ("*7", "B", "F", "A", "7", "C")
option2 = ("A", "7", "C", "B", "F", "*7")
option3 = ("F", "A", "*7", "C", "7", "B") 

while running:
    # Generate random results for 3 reels
    machine = [random.choice(option1), random.choice(option2), random.choice(option3)]

    # Take user investment
    user_investment = int(input("User_investment : "))
    total_investment += user_investment  # add to total investment
 
    print("Machine Result:", machine)

    # Counters for "7" and "*7"
    point1 = 0  # normal 7
    point2 = 0  # special *7

    for symbol in machine:
        if symbol == "7":
            point1 += 1
        elif symbol == "*7":
            point2 += 1

    # Rewards for normal like 7
    if point1 == 3:
        user_coin += 50  
    elif point1 == 2:
        user_coin += 10
    elif point1 == 1:
        user_coin += 5

    # Rewards for special like *7
    if point2 == 3:
        user_coin += 15
    elif point2 == 2:
        user_coin += 10
    elif point2 == 1:
        user_coin += 5    

    # Ask user if they want to continue playing
    your_choice = input("\nIf you want to continue type Y or else type N: ")

    # Exit condition
    if your_choice.lower() == "n":
        running = False

        # Calculate final result when user quits
        profit = user_coin * 10   # coins converted to money
        if profit > total_investment:
            print("Profit:", profit - total_investment)
            print("\n*** PROFIT ***")
        else:
            print("Loss:", total_investment - profit)
            print("\n*** LOSS ***")
