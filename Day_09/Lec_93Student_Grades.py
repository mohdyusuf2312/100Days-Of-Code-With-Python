student_score = {
    "yusuf" : 83,
    "Shuja" : 78,
    "Shadab" : 66,
    "Danish" : 55,
    "Shan" : 20,
    "Farhan" : 92
}

student_grades = {}

for n in student_score:
    if student_score[n] > 90:
        student_grades[n] = "Outstanding"
    elif student_score[n] > 80:
        student_grades[n] = "Excilent"
    elif student_score[n] > 70:
        student_grades[n] = "Acceptable"
    elif student_score[n] > 0:
        student_grades[n] = "Fail"

print(student_grades)