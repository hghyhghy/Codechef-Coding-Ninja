# You are given a string ‘S’. Your task is to return all distinct palindromic substrings of the given string in alphabetical order.

# A string is said to be palindrome if the reverse of the string is the same as the string itself.

# For Example:
# Consider ‘S’ = ‘abba’, all the possible substrings are [ ‘a’, ‘ab’, ‘abb’, 'abba', 'b', ‘ba’, 'bb', ‘bba’ ] out of which [ ‘a’, ‘abba’, 'b’, 'bb'] are palindromic substrings.



def pal(string:str)->bool:
    
    return string.lower() == string[::-1].lower()

def main(string):
    
    n=len(string)

    seen=set()
    
    for i in range(n):
        
        for j in range(i,n):
            
            substring=string[i:j+1]
            
            if pal(substring):
                
                seen.add(substring)

    return sorted(seen)

s = "abba"
print(main(s))