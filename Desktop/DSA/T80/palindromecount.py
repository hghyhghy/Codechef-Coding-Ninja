# You are given a string S of words. Your task is to find the number of palindrome words in the given string S. A word is called palindrome, if it reads the same backwards as forwards.

# Note:
# Words are separated by one or more whitespace characters.
# For Example:
# For the given string “Madam oyo cat”, “Madam”, and “oyo” are the palindrome words 

def check_aplin(sting:str)->bool:
    
    return sting.lower() == sting [::-1].lower()

def main(words:str)->int:
    
    word = words.split()
    
    count  = 0
    for w in word:
        
        if check_aplin(w):
            
            count += 1
            
    return count

S = "Madam oyo cat"
print(main(S))