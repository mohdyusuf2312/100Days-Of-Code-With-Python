dictionary = {
    "a" : "Yusuf",
    "b" : "Shuja",
}
print(dictionary) # it will print complete dictionary

#Add element in the dictionary
dictionary["c"] = "Danish"
dictionary[1] = "Shadab" #Your key may be a number
print(dictionary)

#You ca edit your dictionary
dictionary["c"] = "Shan"
print(dictionary)

#You can create an empty dictionary also
dictionary2 = {}

#Loop on dictionary
for i in dictionary:
    #print(i) # it will print only keys of the dictionary
    print(f"{i} : {dictionary[i]}")