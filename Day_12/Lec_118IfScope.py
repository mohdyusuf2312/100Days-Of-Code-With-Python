banana = 3

if 3>2:         #If statement can't change the boundaries
    banana = 5      #It will update the value even outside the if statement

print(f"Value of banana is {banana}")

#but is the variable store is in local scope then it will never access globally
#for example:

def another():
    pineapple = 9
    if 3>2:
        pineapple = 15
    print(f"Value of banana : {pineapple}")

# print(f"Value of banana : {pineapple}")