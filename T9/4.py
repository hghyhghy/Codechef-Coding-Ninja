# Given a string of lowercase alphabets, count all possible substrings (not necessarily distinct) that have exactly k distinct characters. 

def count_substrings(string,k):
    
    n=len(string)
    count=0
    
    for star in range(n):
        
        store=set()
        
        for end in range(star,n):
            
            store.add(string[end])

            if  len(store) >= k:
                
                count += 1
                
    return count

S = "aba"
K = 2
print(count_substrings(S,K))