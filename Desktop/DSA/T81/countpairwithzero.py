# You are given an array ‘arr’ of ‘N’ integers. Your task is to find the count of pairs with a sum equal to zero.

# Specifically, find the count of all pairs ( i , j ) such that i < j and arr[i] + arr[j] = 0

def count_pairs_with_zero_sum(array:list[int])->int:
    
    n=len(array)
    count  = 0
    
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            if array[i] + array[j] == 0:
                
                count  += 1
                
    return count

arr = [2, -2, 3, -3, 4, -4, 0]
print(count_pairs_with_zero_sum(arr))