print("Welcome to the python pizza! ")
print("Enter S for small pizza : ")
print("Enter M for small pizza : ")
print("Enter L for small pizza : ")
size = input()

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("Invalid Input")

print("Do you want to add pepperoni? Y or N. ")
pep = input()

if pep == "Y" and size == "S":
    bill += 2
if pep == "Y" and (size == "M" or size == "L"):
    bill += 3

print("Do you want to add extra cheese? Y or N. ")
ec = input()

if ec == "Y":
    bill += 1

print("Thank you for choosing Python Pizza Deliveries!")
print(f"Your final bill is: ${bill}")