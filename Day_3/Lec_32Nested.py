print("Wecome to the rollercoaster!")
height = int(input("What is your height in cm ? "))
age = int(input("What is your age? "))

if height > 120:
    print("You can ride the rollercoaster")
    if age < 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("please pay $9")
else:
    print("Sorry, you have to grow taller before you can ride.")

