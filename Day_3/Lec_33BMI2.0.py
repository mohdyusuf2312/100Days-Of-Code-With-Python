height = float(input("Enter height in metre : "))
weight = float(input("Enter weight in kilogram : "))

# height_i = float(height)
# weight_i = float(weight)
BMI = weight / height ** 2

# print("Your BMI is : " + str(BMI))

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you are normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")
