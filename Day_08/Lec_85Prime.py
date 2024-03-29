def check_prime(number):
    if number == 1:
        print(f"{number} is neither prime nor composite")
    elif number < 1:
        print("Invalid input")
    elif number == 2:
        print(f"{number} is only even prime number")
    else:
        for n in range(2,int(number/2)):
            flag = True
            if number % n == 0:
                flag = False
                if flag == False:
                    break
        if flag == False:
            print("Your number is not prime")
        else:
            print("Your number is  prime")
number = int(input("Enter a number : "))
check_prime(number = number)