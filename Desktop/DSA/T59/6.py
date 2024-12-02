# Problem statement
# Given a string, write a program to count the number of vowels, consonants, and spaces in that string.

# EXAMPLE :
# Input: ‘N’= 25, ‘s’ =”Take u forward is Awesome”
# Output: 10 11 4

def count_characaters(string):
    
    vowels=0
    spaces=0
    consonants=0
    
    vowel="aeiouAEIOU"

    for char in string:
        
        if char in vowel:
            
            vowels += 1
            
        elif char == " ":
            
            spaces += 1
            
        elif char.isalpha():
            
            consonants += 1
            
    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")
    print(f"Spaces: {spaces}")

input_string = "Hello, how are you?"
count_characaters(input_string)
