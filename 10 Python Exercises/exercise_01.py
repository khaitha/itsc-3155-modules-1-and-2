grade = input("Enter a grade from 0 to 100: ")
grade = int(grade)

if grade >= 90:
    print("Your grade is A")
if grade < 90 and grade>= 80:
    print("Your grade is B")
if grade <80 and grade >= 70:
    print("Your grade is C")
if grade < 70 and grade >= 60:
    print("Your grade is D")
if grade < 60:
    print("your grade is F")