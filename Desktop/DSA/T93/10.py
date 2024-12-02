#kth most frequenct element 

def main(array,k):
    
    
    freq={}
    for word in array:
        
        if word in freq:
            
            freq[word] += 1
            
        else:
            
            freq[word]=1
            
    
    result=sorted(freq.keys(),key=lambda x:(-freq[x],x))

    return result[:k]

words = ["apple", "banana", "apple", "orange", "banana", "banana"]
k = 2
print(main(words,k))
    