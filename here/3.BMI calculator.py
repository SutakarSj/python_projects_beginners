#BMI calculator 
def calculate_bmi(weight,height):
    bmi = weight / height**2
    return bmi

def bmi_category(bmi):
    if bmi<=18:
        return "Under Weight"
    elif 18.5<=bmi<=24.9:
        return "Normal Weight"
    elif 25<=bmi<=29.9:
        return "Over Weight"
    else:
        return "Obese"

def body_fat_measure(bmi,age,choice,weight):
    men = (1.20 * bmi)+((0.23 * age)-16.2)
    women = (1.20 * bmi)+((0.23 * age)-5.4)
    
    if choice.lower()=='m':
        value=men/100
        grams=weight*1000
        male=(grams*value)
        return int(male/1000)
    
    if choice.lower()=='f':
        value=women/100
        grams=weight*1000
        female=(grams*value)
        return int(female/1000)
       
def main():
    try:
        weight=float(input("Enter your Weight in kilograms: "))
        height=float(input("Enter your Height in METERs: "))        
        if weight<=0 or height<=0:
            print("ERROR, the entered value got error")
            return 
        
        age=int(input("Enter your age: "))
        choice=input("Enter your choice (male-M or female-F): ")
        
        bmi = calculate_bmi(weight,height)
        category = bmi_category(bmi)
        fat = body_fat_measure(bmi,age,choice,weight)
        
        print(f"\nBMI value is: {bmi:.2f}")
        print(f"category: {category}")
        print(f"\nYour body fat: {fat}Kg")
    
    except ValueError:
        print("ERROR: Invalid Input. please enter numeric value")
    
if __name__ == "__main__":
    main()