'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def pairwise_product(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Both lists must have equal length.")
    
    result = []
    for i in range(len(list1)):
        product = list1[i] * list2[i]
        result.append(product)
    
    return result

# Ask users to input the two lists separated by commas
list1_input = input("Enter the first list separated by commas: ")
list1 = [int(num) for num in list1_input.split(",")]

list2_input = input("Enter the second list separated by commas: ")
list2 = [int(num) for num in list2_input.split(",")]

result = pairwise_product(list1, list2)
print("Pairwise product of the two lists:", result)
