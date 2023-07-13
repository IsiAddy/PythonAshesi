'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def is_triangle(a, b, c):
 if a>b+c or b>a+c or c>b+a:
  return False
 else:
      return True
a = float(input("Enter the value for triangle 1: ")) 
b = float(input("Enter the value for triangle 2: "))
c = float(input("Enter the value for triangle 3: "))
if is_triangle(a,b,c):
   print("Yes you can form the triangles ")
else:
    print("No, you can't form the triangles")