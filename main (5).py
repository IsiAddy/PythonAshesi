'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
P = 10000
n = 12
r = 0.08
t = int(input("Enter the time in years ? "))

A = P * (1+ r/n) ** (n*t)

print("The final amount is", A)
