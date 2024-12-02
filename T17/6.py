# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

def k_most_frequent_elements(array,k):
    
    freq={}

    for num in array:
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] = 1
            
            
    temp_sets=sorted(freq.items() , key= lambda x:x[1],reverse=True)

    top_k=[item[0] for item in temp_sets[:k]]
    
    return top_k


nums = [1, 1, 1, 2, 2, 3]
k = 2

print(k_most_frequent_elements(nums,k))