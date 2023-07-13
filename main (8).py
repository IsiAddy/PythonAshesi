'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def calculateGPA(score):
    if 85 <= score <= 100:
        return 4.0
    elif 80 <= score <= 84:
        return 4.0
    elif 75 <= score <= 79:
        return 3.5
    elif 70 <= score <= 74:
        return 3.0
    elif 65 <= score <= 69:
        return 2.5
    elif 60 <= score <= 64:
        return 2.0
    elif 55 <= score <= 59:
        return 1.5
    elif 50 <= score <= 54:
        return 1.0
    else:
        return 0.0


def getHonours(GPA):
    if 3.85 <= GPA <= 4.0:
        return "Summa Cum Laude"
    elif 3.70 <= GPA <= 3.84:
        return "Magna Cum Laude"
    elif 3.50 <= GPA <= 3.69:
        return "Cum Laude"
    else:
        return "No Honours"


score = float(input("What is your score? "))
GPA = calculateGPA(score)
honours = getHonours(GPA)

print("GPA is", GPA)
print("Honours is", honours)
