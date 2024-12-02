# You are given an array ‘ARR’ and another integer number ‘K’. Your task is to find the all elements of ‘ARR’ which occur more than or equals to ‘N/K’ times in ‘ARR’ and ‘N’ is the length of array ‘ARR’.

def majority_element(array,k):
    
    n=len(array)
    if k >= n:
        
        return []

    freq={}
    for num in array:
        
        if num in freq:
            
            freq[num]  += 1
            
        else:
            
            freq[num] = 1
            
    threshold = n//k
    
    result= [num for num,count in freq.items() if count >= threshold]

    return result

arr = [1, 2, 3, 1, 1, 2, 4, 4, 4, 4]
K = 3
print(majority_element(arr,K))