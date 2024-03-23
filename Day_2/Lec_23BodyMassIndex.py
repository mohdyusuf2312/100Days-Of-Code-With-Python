height = input("Enter height in metre : ")
weight = input("Enter weight in kilogram : ")

height_i = float(height)
weight_i = float(weight)
BMI = int(weight_i / height_i ** 2)

print("Your BMI is : " + str(BMI))