year = int(input("Enter year: "))
month = input("Enter month: ").lower()

def is_leap(leap):
    if (leap % 4 ==0 and leap % 100 != 0) or leap % 400 == 0 :
        return True
    else:
        return False
    
leap = {"jan":31,"feb":29,"mar":31,"apr":30,"may":31,"jun":30,"jul":31,"aug":31,"sep":30,"oct":31,"nov":30,"dec":31}
not_leap = {"jan":31,"feb":28,"mar":31,"apr":30,"may":31,"jun":30,"jul":31,"aug":31,"sep":30,"oct":31,"nov":30,"dec":31}

if is_leap(year) == True:
    print(f"{leap[month]} days in {month}")
else:
    print(f"{not_leap[month]} days in {month}")