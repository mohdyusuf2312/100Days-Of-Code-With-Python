print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
Tip = int(input("How much tip would you like to give? 10%, 12%, or 15% ? "))
people = int(input("How many people to split the bill ? "))

Tip = ((Tip)/100)*bill
amnt = bill + Tip
perH = round((amnt/people),2)
# perH = round(perH,2)

print(f"Each person should pay : {perH}")