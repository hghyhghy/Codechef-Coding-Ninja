# Problem statement
# You are given an Integer array ‘ARR’ and an Integer ‘K’.



# Your task is to find the ‘K’ most frequent elements in ‘ARR’. Return the elements in any order.



# For Example:

# You are given ‘ARR’ = {1, 2, 2, 3, 3} and ‘K’ = 2. 

# The answer will {2, 3} as 2 and 3 are the elements occurring most times.

def top_k_frequent_element(array:list[int],k:int)->list[int]:
    
    freq={}
    for num in array:
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] = 1
            
    new_element =  sorted(freq,key=lambda x : freq[x], reverse=True)
    
    return new_element[:k]

arr = [1, 2, 2, 3, 3]
k = 2

print(top_k_frequent_element(arr,k))