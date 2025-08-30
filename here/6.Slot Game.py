#Slot Game 
import random

running=True

user_amount=0
user_coin=0

option1=("*7","B","F","A","7","C")
option2=("A","7","C","B","F","*7")
option3=("F","A","*7","c","7","B")
 
while running:
    machine=[0]*3
    machine[0]=random.choice(option1)
    machine[1]=random.choice(option2)
    machine[2]=random.choice(option3)

    user_inversment=int(input("User_inversment :"))
    user_amount=user_inversment//10

    print(machine)

    point1=0
    point2=0

    for i in range(len(machine)):
        if machine[i]=="7":
            point1+=1
        elif machine[i]=="*7":
            point2+=1
            
    if point1!=0:
        if point1==3:
            user_coin+=50
        elif point1==2:
            user_coin+=10
        elif point1==1:
            user_coin+=5
            
    if point2!=0 or point2!=1:
        if point2==3:
            user_coin+=15
        elif point2==2:
            user_coin+=10
        elif point2==1:
            user_coin+=5    
    print("\nIf you want to continue type Y or else type N")
    your_choice=input()

    if your_choice.lower()=="y":
        running=True
    if your_choice.lower()=="n":
        running=False
        
profit=(user_coin * 10) + user_amount

if profit > user_amount:
    print("Profit :",profit)
    print("\n***PROFIT***")

else:
    print("Loss :",profit)
    print("\n***LOSS***")