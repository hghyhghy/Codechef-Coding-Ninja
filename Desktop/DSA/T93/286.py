

#kth most frequent element 

def main(array,k):
    
    freq={}

    for num in array:
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] = 1
            
    
    result=sorted(freq.keys(),key=lambda x:(-freq[x],x))

    return result[:k]

words = ["apple", "banana", "apple", "orange", "banana", "banana"]
k = 2

print(main(words,k))