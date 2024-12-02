# Problem statement
# You have been given an integer array/list(arr) and a number 'Sum'. Find and return the total number of pairs in the array/list which when added, results equal to the 'Sum'.

# Note:
# Given array/list can contain duplicate elements.

# # (arr[i],arr[j]) and (arr[j],arr[i]) are considered same.

def pair_with_given_sum(array:list[int],target:int)->int:
    
    n=len(array)
    count = 0
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            if array[i]+array[j] == target:
                
                count +=1
                
    return count

arr = [1, 2, 3, 4, 3]
Sum = 6

print(pair_with_given_sum(arr,Sum))