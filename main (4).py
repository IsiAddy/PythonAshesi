'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
hwWeight = 0.4

examWeight = 0.5

discussionWeight = 0.1

homework_grade = float (input ("What is your homework grade? "))
exam_grade = float (input("What is your exam grade? "))
discussion_weight = float (input("What is your discussion weight? "))

real_homework_grade = hwWeight * homework_grade
real_exam_grade = examWeight * exam_grade
real_discussion_weight = discussionWeight * discussion_weight

total_grade = real_homework_grade + real_exam_grade + real_discussion_weight
print("Your total grade is", total_grade)