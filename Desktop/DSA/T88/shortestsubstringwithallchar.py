# You have been given a string 'S' which only consists of lowercase English-Alphabet letters.

# Your task is to find the shortest(minimum length) substring of 'S' which contains all the characters of 'S' at least once. If there are many substrings with the shortest length, then find one which appears earlier in the string i.e. substring whose starting index is lowest.

# For example-
# If the given string is S = "abcba", then the possible substrings are "abc" and "cba". As "abc" starts with a lower index (i.e. 0, "cba" start with index 2), we will print "abc" as our shortest substring that contains all characters of 'S'.

def shortest_substring_with_all_char(string:str)->str:
    
    n=len(string)
    seen=set(string)
    min_len=float("inf")
    result=""

    for start in range(n):
        
        for end in range(start+1,n+1):
            
            substring= string[start:end]
            
            if set(substring) ==  seen:
                
                if len(substring)<min_len:
                    
                    min_len = len(substring)
                    result =substring
                    break
                
    return result

S = "abcba"
print(shortest_substring_with_all_char(S))