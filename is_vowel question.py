'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def is_vowel(character):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if character.lower() in vowels:
      return True
    else:
        return False
character = input("Enter your character  ")
result =is_vowel(character)
print(result)
    