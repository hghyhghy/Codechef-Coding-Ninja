

#minimum char to make palindrome

def main(string):
    
    n=len(string)

    reversed_string=string[::-1]

    for i in range(n):
        
        if string[i:] == reversed_string[:n-i]:
            
            return i
        
    
    return -1

STR1 = "abcd"
print(main(STR1))