# You are given an array ‘ARR’ containing ‘N’ integers, and you are also given an integer ‘TARGET’.

# You task is to find the count of triplets i, j, k ( 0 ≤ i < j < k < N ), such that 'ARR[i]' + 'ARR[j]' + 'ARR[j]' is less than the value of ‘TARGET’.

# For Example :
# If ‘N’ = 7, ‘ARR’ = { 1, 5, 2, 3, 4, 6, 7 } and ‘TARGET’ = 9


def count_triplets_less_than_target(array:list[int],target:int)->int:
    
    n=len(array)
    count  = 0
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            for k in range(j+1,n):
                
                if array[i]+array[j]+array[k] <  target:
                    
                    count +=1
                    
    return count

arr = [1, 5, 2, 3, 4, 6, 7]
target = 9
print(count_triplets_less_than_target(arr,target))
