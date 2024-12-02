# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

def top_k_frequent_elements(array,k):
    
    freq={}

    for num in array:
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] = 1
            
    
    new = sorted(freq.items(), key=lambda x : x[1], reverse=True)

    result=[item[0] for item in new[:k] ]
    
    return result

nums = [1, 1, 1, 2, 2, 3]
k = 2
print(top_k_frequent_elements(nums,k))