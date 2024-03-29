height = int(input("Enter height : "))
width = int(input("Enter width : "))
coverage = 5
def paint_calc(height, width, coverage):
    paint = (height*width)/coverage
    return paint
    

n = paint_calc(height = height, width = width, coverage = coverage)
print(f"number of can use : {n}")