# Given an array 'arr' of 'N' integers and an integer 'K'. The array 'arr' may contain duplicate integers. Return "true" if the array contains any duplicate element within the 'K' distance from each other, otherwise, return "false".

def conatins_duplicate_at_k_distance(array:list[int],k:int)->bool:
    
    n=len(array)

    for i in range(n):
        
        for j in range(i+1,min(i+k+1,n)):
            
            if array[i] ==  array[j]:
                
                return True
            
    return False

arr = [1, 2, 3, 1, 2, 3]
k = 3
print(conatins_duplicate_at_k_distance(arr,k))