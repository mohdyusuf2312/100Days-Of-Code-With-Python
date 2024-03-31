print("Wecome to the rollercoaster!")
height = int(input("What is your height in cm ? "))
age = int(input("What is your age? "))

if height > 120:
    print("You can ride the rollercoaster")
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 9
        print("Adult tickets are $9")
    want_photo = input("Do you wnt a photo taken? Y or N. ")
    if(want_photo == "Y"):
        bill += 3
    
    print(f"Please pay ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")

