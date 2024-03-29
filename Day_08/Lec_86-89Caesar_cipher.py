list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
from Caesar_cipher_logo import logo
print(logo)
def encrypt(text, shift):
    encrypt = []
    for letter in range(len(text)):
        if text[letter] in list:
            index = list.index(text[letter])
            encrypt.append(list[index+shift])
        else:
            encrypt.append(text[letter])
    print(f"{''.join(encrypt)}")
    run = input("Do you want to run again type 'Y' for yes and type 'N' for no : ").lower()
    if run == "y":
        main()
    elif run == "n":
        print("Okay Goodbye!")

def decrypt(text, shift):
    decrypt = []
    for letter in range(len(text)):
        if text[letter] in list:
            index = list.index(text[letter])
            decrypt.append(list[index-shift])
        else:
            decrypt.append(text[letter])
    print(f"{''.join(decrypt)}")
    run = input("Do you want to run again type 'Y' for yes and type 'N' for no : ").lower()
    if run == "y":
        main()
    elif run == "n":
        print("Okay Goodbye!")
    
def main():
    direction = input("Type 'encrypt' or 'decrypt' : ")
    text = input("Enter your message : ").lower()
    shift = int(input("Type shift number : "))
    shift %= 26
    
    if direction == "encrypt":
        encrypt(text = text, shift = shift)
    elif direction == "decrypt":
        decrypt(text = text, shift = shift)
    else:
        print("Invalid input")

main()