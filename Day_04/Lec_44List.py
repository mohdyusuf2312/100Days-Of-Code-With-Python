#List
list = ["apple", "America","khan",1,1,3,2]
print(list[2]) #output khan

#There are many functions that are performs on the lsit

list.append("Khan") #Add new element in the end of the lsit
print(list)

list.extend("khan") #Add every character of attribute in the end of the lsit
print(list) # output : ['apple', 'America','khan',1,1,3,2,'khan','k','h','a','n']

list.insert(5,'Yusuf') #Add element via index value
print(list) #output : ['apple', 'America','khan',1,1,'Yusuf',3,2,'khan','k','h','a','n']

list.remove(1) #remove first element whose value equal to 1
list.pop(-1) # remove via index value

list.clear() #remove all elements of the list

list.count('yusuf') #counts number of yusuf present in the list

list.sort(reverse = True) #reverse the list

list1 = [1,2,3]
list2 = [4,5,6]
list3 = [list1,list2]
print(list3) #output : [[1,2,3],[4,5,6]]
print(list3[1][2]) #Output : 6