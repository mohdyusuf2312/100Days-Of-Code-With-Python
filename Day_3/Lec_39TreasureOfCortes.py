print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
      ''')

# print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
# move1 = input("Right or left? ")
# move1 = move1.lower()
# if move1 == "right":
#     print("Game Over.")
# elif move1 != "right" and move1 != "left":
#     print("Invalid input!")
# else:
#     print("Swim or wait? ")
#     move2 = input()
#     move2 = move2.lower()
#     if move2 == "swim":
#         print("Game Over.")
#     elif move2 != "swim" and move2 != "wait":
#         print("Invalid input!")
#     else:
#         print("Which door? Red, Blue, or Yellow ")
#         move3 = input()
#         move3 = move3.lower()
#         if move3 == "red" or move3 == "blue":
#             print("Game Over.")
#         elif move3 == "yellow":
#             print("You Win!")
#         else:
#             print("Invalid input")

            #Alternate

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
move1 = input("You\'re at crossroad, Where do you want to go? Type 'left' or 'right'.").lower()
if move1 == "right":
    print("Game Over! You move to the wrong way.")
elif move1 != "right" and move1 != "left":
    print("Invalid input!")
else:
    move2 = input("You\'ve come to lake. There is an Island  in the middle of the lake. Type 'Swim' to swim across or type 'wait' to wait for a boat.").lower()
    if move2 == "swim":
        print("Game Over! You got attacked by an angry trout.")
    elif move2 != "swim" and move2 != "wait":
        print("Invalid input!")
    else:
        move3 = input("Now you arrive at the island unharmed. There is a house with three doors. One red, one yellow and one blue. Which color do you choose?").lower()
        if move3 == "red" or move3 == "blue":
            print("Game Over! You got attacked by the zombies.")
        elif move3 == "yellow":
            print("You Win! You found the treasure.")
        else:
            print("Invalid input")