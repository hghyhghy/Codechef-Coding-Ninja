

#k th most frequent element

def main(array,k):
    
    freq={}
    for num in array:
        
        if num in freq:
            
            freq[num] +=1
            
        else:
            
            freq[num] =1
            
            
    temp= sorted(freq.items(),key=lambda x:x[1], reverse=True)

    top=[item[0] for item in temp[:k]]

    return top

nums = [1, 1, 1, 2, 2, 3]
k = 2

print(main(nums,k))