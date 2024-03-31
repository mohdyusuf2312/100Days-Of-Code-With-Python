list1 = ["⬜️","⬜️","⬜️"]
list2 = ["⬜️","⬜️","⬜️"]
list3 = ["⬜️","⬜️","⬜️"]
map = [list1, list2, list3]
print("Hiding your treasure! X marks the spot.")
position = input()
lttr = position[0].lower()
abc = ["a", "b", "c"]
lttr_index = abc.index(lttr)
num_index = int(position[1]) - 1
map[num_index][lttr_index] = "X"

print(f"{list1}\n{list2}\n{list3}")

# map[[1][1]]  
# map[1][1]
# these both instructions have different meaning