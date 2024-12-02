# Problem statement
# You are given a binary array 'arr' of length 'N' and an integer 'k'. Return the number of subarrays having the count of 1's equal to ‘k’.



# Example :
# Let the array 'arr' be: [1, 0, 1].
# Let ‘k’ be: 1

# Then the subarrays having the number of ones equal to ‘k’ will be: [1], [1,0], [0,1], [1].

def count_subarray(array:list[int],k:int)->int:
    
    n=len(array)
    result= 0
    
    
    for i in  range(n):
        count = 0
        for j in range(i,n):
            
            if array[j] == 1:
                
                count  += 1
                
                
            if count == k:
                
                result += 1
                
    return result

arr = [1, 0, 1]
k = 1
print(count_subarray(arr,k))
                