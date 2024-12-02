# You are given two strings S and X containing random characters. Your task is to find the smallest substring in S which contains all the characters present in X.

# Example:

# Let S = “abdd” and X = “bd”.

# The windows in S which contain all the characters in X are: 'abdd', 'abd', 'bdd', 'bd'. 
# Out of these, the smallest substring in S which contains all the characters present in X is 'bd'. 
# All the other substring have a length larger than 'bd'.

def smallest_substring(s:str,x:str)->str:
    
    seen=set(x)
    n=len(s)

    smallest=None
    
    for i in range(n):
        
        for j in range(i+1,n+1):
            
            substring  = s[i:j]

            if seen.issubset(set(substring)):
                
                if smallest is None or len(substring) < len(smallest):
                    
                    smallest = substring
                    
    return smallest if smallest else " "

s = "abdd"
x = "bd"
print(smallest_substring(s,x))