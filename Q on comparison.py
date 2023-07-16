'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def compareStrings(garland, flowers):
    inboth = 0
    for flower in flowers:
        if flower in garland:
            inboth += 1
    return inboth
garland = "abcde"
flowers = "abfgcdhi"
result = compareStrings(garland, flowers)
print(result)