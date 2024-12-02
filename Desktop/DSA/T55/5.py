# Find the majority element in the array. A majority element in an array A[] of size n is an element that appears more than n/2 times (and hence there is at most one such element). 

# Examples : 

# Input : arr[] = {3, 9, 2, 9, 2, 9, 9}
# Output : 9
# Explanation: n = 7. Note that 9 appear more 4 times which is more than 7/2 times 

# Input : arr[] = {3}
# Output : 3
# Explanation: Appears more than n/2 times

# Input : A[] = {3, 3, 4, 2, 4, 4, 2, 4}
# Output : No Majority Element
# Explanation: There is no element whose frequency is greater than the half of the size of the array size.

def majority_element(array):
    
    freq={}
    n=len(array) 
    
    for num in array:
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] = 1
            
    
    limit= n//2
    
    for num,count in freq.items():
        
        if count > limit:
            
            return num
    
    return None

arr = [3, 9, 2, 9, 2, 9, 9]
print(majority_element(arr))