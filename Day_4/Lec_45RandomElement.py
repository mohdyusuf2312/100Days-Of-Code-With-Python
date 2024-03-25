import random
names_str = input("Enter all the names : ")
names = names_str.split(", ")
len = names.__len__()
ran = random.randint(0,len-1)
pay = names[ran]
print(f"Person who will pay : {pay}")