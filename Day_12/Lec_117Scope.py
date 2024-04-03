apple = 1

def increase():
    apple = 2
    print(f"value of apple inside the method : {apple}")

increase()
print(f"value of apple outside the method : {apple}")

# apple whose value == 1 is in the global scope while apple whose value == 2 is in local scope

def another():
    banana = 3
    print(f"Value of banana : {banana}")

# print(f"Value of banana : {banana}")

# in the another function, banana == 3 which is in local scope.
#You can't access the local variable in different method aur in globally, while
#global variable can access from anywhere in the program

