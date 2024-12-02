# Problem statement
# Ninja has been given a string ‘WORD’ containing lowercase English alphabets having length ‘N’. Ninja wants to calculate the number of distinct substrings in the ‘WORD’.

# For Example :

# For ‘WORD’ = “abcd” and ‘N’ = 4 following are the 10 distinct substrings of ‘WORD’.
# “abcd”, “abc”, “ab”, “a”, “bcd”, “bc”, “b”, “cd”, “c”, and “d”
# Can you help the Ninja to find out the number of distinct substrings in the ‘WORD’?

# Note :

# If you are going to use variables with dynamic memory allocation then you need to release the memory associated with them at the end of your solution.

def count_of_distinct_substrings(string:str)->int:
    
    n=len(string)
    
    seen=set()
    
    for i in range(n):
        
        char = ""
        
        for j in range(i,n):
            
            char += string[j]
            
            seen.add(char)
            
    return len(seen)

word1 = "abcd"
print(count_of_distinct_substrings(word1))
            
            