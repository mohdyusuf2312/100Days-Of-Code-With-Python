#Day_09

dict = {}
import os

def clear_console():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Unix-like systems (Linux, macOS)
    else:
        _ = os.system('clear')
# Call the function to clear the console

def highest():
    highest_bid = 0
    winner = ""
    for n in dict:
        bid = dict[n]
        if bid > highest_bid:
            highest_bid = bid
            winner = n
    print(f"The winner is {winner} with a bid of ${highest_bid}")

bidding_finished = False
while bidding_finished == False:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid price: "))
    dict[name] = bid
    other = input("Is there are other users who want to bid: Type 'yes' or 'no' : ").lower()
    if other == "yes":
        clear_console()
    if other == "no":
        highest()
        bidding_finished = True