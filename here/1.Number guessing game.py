#number guessing game
import random

random_value = random.randint(1, 50)
count=0
while (count != 5):
    user_input=int(input("\nENTER NUMBER:"))
    
    if (user_input == random_value):
        print("    $$$ WINNER $$$")
        break
       
    elif (user_input<random_value and user_input<=50):
        print("    GREATER THAN YOUR INPUT")
        count+=1
       
    elif (user_input>random_value and user_input<=50):
        print("    LESS THAN YOUR INPUT")
        count+=1
    
    else:
       print("    INVALIDE VALUE")
        
if (count==5 and user_input!=random_value):
    print("\n    ---YOU LOSS---")
    
print("\ncomputer value:",random_value)
print("\nTotal count:",count)