height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

new_bmi = round((weight) / (height ** 2))

if new_bmi < 18.5:
    print(f"Your BMI is {new_bmi}, you are underweight.")
elif new_bmi > 18.5 and new_bmi < 25:
    print(f"Your BMI is {new_bmi}, you have a normal weight.")
elif new_bmi >25 and new_bmi <30:
    print(f"Your BMI is {new_bmi}, you are slightly overweight.")
elif new_bmi >30 and new_bmi <35:
    print(f"Your BMI is {new_bmi}, you are obese.")
else:
    print(f"Your BMI is {new_bmi}, , you are clinically obese.")
