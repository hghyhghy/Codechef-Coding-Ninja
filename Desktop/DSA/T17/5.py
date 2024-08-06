# longest common string without repeating character using native brute force approach without using DP

def longest_substring_unique(string):
    
    def is_unique(string):
        
        return len(string) == len(set(string))


    n=len(string)
    max_length=0
    longest_string=""

    for start in range(n):
        
        for end in range(start+1,n+1):
            
            substring = string[start:end]

            if is_unique(substring):
                
                if len(substring) > max_length:
                    
                    max_length = len(substring)
                    longest_string =  substring
                    
    return longest_string

s = "abcabcbb"
print(longest_substring_unique(s))