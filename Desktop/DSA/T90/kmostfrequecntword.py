# You have been given an array/list 'WORDS' of 'N' non-empty words, and an integer 'K'. Your task is to return the 'K' most frequent words sorted by their frequency from highest to lowest.

# Note:

# If two words have the same frequency then the lexicographically smallest word should come first in your answer.

def k_most_frequenct_word(array:list[str],k:int)->list[str]:
    
    freq={}
    
    for word in array:
        
        if word in freq:
            
            freq[word]+=1
            
        else:
            
            freq[word] =1
            
    
    
    result=sorted(freq.keys() ,key=lambda x:(-freq[x],x))
    
    return result[:k]

words = ["apple", "banana", "apple", "orange", "banana", "banana"]
k = 2
print(k_most_frequenct_word(words,k))