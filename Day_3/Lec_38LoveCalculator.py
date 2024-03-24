print("Welcome to the Love Calculator! ")
name1 = input("Enter your name : ")
name2 = input("Enter your partner name : ")
print("The Love calculator is calculating your score...")

Comb_name = name1 + name2
lowername = Comb_name.lower()

t = lowername.count("s")
r = lowername.count("f")
u = lowername.count("u")
e = lowername.count("h")
first_digit = t+r+u+e

l = lowername.count("l")
o = lowername.count("o")
v = lowername.count("v")
e = lowername.count("e")
second_digit = l+o+v+e

print(f"Your score is : {first_digit}{second_digit}%")