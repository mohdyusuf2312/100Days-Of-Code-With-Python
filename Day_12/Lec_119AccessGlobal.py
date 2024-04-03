apple = 1

#Example 1:
def increase():
    apple = 2 #If you write like this, then it is okay
    print(f"value of apple inside the method : {apple}")

#Example 2:
def increase():
    apple += 1      #There is a error, this method can't recognise the apple 
    print(f"value of apple inside the method : {apple}")

#Example 3:
def increase():
    global apple        #You have to write global
    apple += 1          #now caompiler recognise the global apple
    print(f"value of apple inside the method : {apple}")

#Example 4:
def increase():
    # global apple += 1         #You can't write like this
    #this will give you an error that line must be seperated
    print(f"value of apple inside the method : {apple}")

#Example 5:
#But you can return like this
def increase():
    # apple = 2 #If you write like this, then it is okay
    print(f"value of apple inside the method : {apple}")
    return apple + 1

increase()
print(f"value of apple outside the method : {apple}")