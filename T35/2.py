# longest substring without repeating chars

def longest_substring_without_repeating_char(string):
    
    max_lenght= 0
    
    n=len(string)

    for i in range(n):
        
        store=set()
        count = 0
        
        
        for j in range(i,n):
            
            if string[j] in store:
                
                break
            
            store.add(string[j])

            count += 1
            
        max_lenght=max(max_lenght,count)

    
    return max_lenght

s = "abcabcbb"
print(longest_substring_without_repeating_char(s))