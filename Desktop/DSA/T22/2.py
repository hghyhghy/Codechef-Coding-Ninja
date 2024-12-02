# check if there are vowels are present 

def contain_vowels(string):
    
    vowels=set('aeiouAEIOU')

    for char in string:
        
        if char in vowels:
            
            return True
        
    return False

word = "hello"
print(contain_vowels(word))

