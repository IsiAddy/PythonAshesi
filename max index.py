'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def max_index(numbers):
    numbers_list = [int(num) for num in numbers.split(",")]
    max_value = max(numbers_list)
    max_index = numbers_list.index(max_value)
    return max_index


numbers_list = input("Enter the numbers? ")
result = max_index(numbers_list)
print("The index of the largest value is", result)
