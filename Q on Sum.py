'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def calculatefrom1(number):
    sumfrom1 = 0
    for i in range(1, number+1):
      sumfrom1 += i
    return sumfrom1
number = int(input("Please enter a number? "))
answer = calculatefrom1(number)
print(answer)