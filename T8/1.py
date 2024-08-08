
# longest sustring without repeating chars

def longest_substring_without_repeating(string):
    
    n=len(string)
    char=set()
    start=0
    lenght = 0
    
    
    for end in range(n):
        
        while string[end] in char:
            
            char.remove(string[start])
            start += 1
            
        
        char.add(string[end])
        lenght = max(lenght,end-start +1)

    return lenght

s = "abcabcbb"
print(longest_substring_without_repeating(s))