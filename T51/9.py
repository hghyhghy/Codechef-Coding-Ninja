# Problem statement
# Given an array 'arr' of 'N' integers and an integer 'K'. The array 'arr' may contain duplicate integers. Return "true" if the array contains any duplicate element within the 'K' distance from each other, otherwise, return "false".

def contains_duplicate_from_k_distance(array,k):
    
    seen=set()
    n=len(array)

    if not array or n<k:
        
        return 
    
    for i in range(n):
        
        for  j in range(i,i+k):
            
            if array[j] in seen:
                
                return True
            
            else:
                
                seen.add(array[j])

    return False

arr = [1, 2, 3, 1]
K = 3

print(contains_duplicate_from_k_distance(arr,K))