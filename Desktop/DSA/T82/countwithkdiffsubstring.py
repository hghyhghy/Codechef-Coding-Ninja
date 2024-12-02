# Problem statement
# You are given a string 'str' of lowercase alphabets and an integer 'k' .



# Your task is to return the count all the possible substrings that have exactly 'k' distinct characters.



# For example:

# 'str' = abcad and 'k' = 2. 

# We can see that the substrings {ab, bc, ca, ad} are the only substrings with 2 distinct characters. 

# Therefore, the answer will be 4.   

def count_with_k_difference_substring(string:str,k:int)->int:
    
    n=len(string)
    count = 0
    
    
    for start in range(n):
        
        for end in range(start,n):
            
            substring =  string[start:end+1]
            
            distinct= set(substring)
            
            if len(distinct) == k:
                
                count += 1
                
    return count

s = "abcad"
k = 2
print(count_with_k_difference_substring(s,k))