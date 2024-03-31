#Random
import random
while input("Enter t for toss the coin : ").lower() == "t":
    rand_num = random.randint(1,2)
    if rand_num == 1:
        print("Its Head")
    else:
        print("Its tell")