# One day Ninja got an array and started to play with it. He is finding subarrays of the array randomly and suddenly starts to wonder about the maximum of the sum of the smallest and the second smallest elements of all the subarrays possible of size at least 2.

# For Example:
# For the array [3 2 1]
# All the subarrays of size at least 2 are:
# [3 2], [2 1], [3 2 1]
# For the first subarray, the smallest and second smallest elements are 2 and 3, and their sum is 5.
# For the second subarray, the smallest and second smallest elements are 1 and 2, and their sum is 3.
# For the third subarray, the smallest and second smallest elements are 1 and 2, and their sum is 3.
# So the maximum among these sums is 5.
# Since Ninja is too lazy to do this task, he asked you for help. You have to find the maximum of the sum of the smallest and the second smallest elements of all the subarray possible of size at least 2.

def smallest_sum_subarray(array:list[int])->int:
    
    n=len(array)

    max_one=float("-inf")
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            subarray =  array[i:j+1]
            
            if len(subarray)>=2:
                
                sorted1= sorted(subarray)
                smallest =sorted1[0]
                
                smallest_second=  sorted1[1]
                
                total = smallest+smallest_second
                
                max_one = max(max_one,total)

    return max_one
 
arr = [3, 2, 1]
print(smallest_sum_subarray(arr))