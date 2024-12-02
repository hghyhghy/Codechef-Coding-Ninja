# Problem statement
# You are given a string 'STR' containing lowercase English letters from a to z inclusive. Your task is to find all non-empty possible subsequences of 'STR'.

# A Subsequence of a string is the one which is generated by deleting 0 or more letters from the string and keeping the rest of the letters in the same order.

def subsequence_of_string(string:str)->str:
    
    subsequence=[]
    
    n=len(string)
    
    for start in range(n):
        
        for end in range(start,n):
            
            substring =  string[start:end+1]
            
            subsequence.append(substring)

    return " ".join(subsequence)

STR = "abc"
print(subsequence_of_string(STR))
            
        