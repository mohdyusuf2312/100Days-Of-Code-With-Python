import random
letters = ['a','b','c','d','e','f','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','-','_','=','+','~','`',',','<','.','>','/','?','\'','\"',';',':','[',']','{','}','\\','|']

print("Welcome to the Password Generator! ")
req_lttr = int(input("How many letters would you like in your password: "))
req_num = int(input("How many number would you like in password: "))
req_sym = int(input("How many symbols would you like in your password: "))

n=0
while n<10000000/2:
    if n == 1:
        print("Your password is generating...")
    n+=1
print()

# password = ""
# for char in range(0,req_lttr):
#     password += random.choice(letters)

# for num in range(0,req_num):
#     password += random.choice(numbers)

# for sym in range(0,req_sym):
#     password += random.choice(symbols)

# print(f"Here is your password : {password}")
    
    # output : gjdA09@)


    #alternate

password_list = []

for char in range(0,req_lttr):
    password_list.append(random.choice(letters))

for num in range(0,req_num):
    password_list.append(random.choice(numbers))

for sym in range(0,req_sym):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
password = ""
for x in password_list:
    password += x
print(f"Here is your password : {password}")