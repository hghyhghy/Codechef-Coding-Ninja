# You are given a string ‘S’. You are also given ‘M’ integers in an array ‘A’. You perform ‘M’ operations on this string. The operations are given in an array ‘A’ of size ‘M’.

# You perform the operations in the order they appear in the array ‘A’. In the ‘i’th operation, you reverse the substring of ‘S’ from the position ‘A[i]’ to ‘len(S)’ - ‘A[i]’ - 1 (0 based).

# Your task is to find the string after performing all the operations.

# Example :
# ‘S’ = “aabcd”, ‘M’ = 2, ‘A’ = [0, 1]
# After 1st operation i.e, reversing from [0, 4], ‘S’ = “dcbaa”.
# After 2nd operation i.e, reversing from [1, 3], ‘S’ = “dabca”.
# Hence, the answer is “dabca”.

def feverse_string_in_range(string:str,a:list[int])->str:
    
    s=list(string)

    for i in a:
        
        left=i
        right=len(s)-i-1
        
        while left < right:
            
            s[left],s[right]=s[right],s[left]
            
            left +=1
            right -=1
            
    return "".join(s)

S = "aabcd"  # The original string
A = [0, 1]   # The array of operations
print(feverse_string_in_range(S,A))