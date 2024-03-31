# Day_10

f_name = input("Enter first name: ")
l_name = input("Enter last name: ")

def title_f(f_name, l_name):
    fi_name = f_name.title()
    la_name = l_name.title()
    return (f"{fi_name} {la_name}")

title = title_f(f_name, l_name)
print(title)