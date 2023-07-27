'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def min_index(numbers):
    min_value = min(numbers)
    min_index = numbers.index(min_value)
    return min_index


numbers_list = input("Enter the numbers? ")
result = min_index(numbers_list)
print("The index of the smallest value is", result)