height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

BMI = weight / (height/100) ** 2

print("Your BMI is", BMI)

if BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are over weight.")
elif BMI <= 34.9:
    print("You are severely over weight.")
elif BMI <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")
num = int(input("Enter number to check :"))
if num>50:
    print("Number is greater than 50")
    if num%2 == 0:
        print("And it is even too")
    else:
        print("And it is odd")
else:
    print("Number is less than 50")