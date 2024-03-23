num_char = len(input("What is your name : "))
print("Your name contains " + str(num_char) + " characters.")

#typeCasting
#str(num_char) In this line num_char has an integer value, but you can't concatenate integer with string that is you have to typecaste the variable
# In the above line; num_char is typecasted as a string

print(70 + float("100.5"))  #output : 170.5

print(str(70) + str(100)) #output : 70100