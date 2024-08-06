# The function accepts an integer array ‘arr’ of size ‘n’ as its argument. The function needs to return the index of an equilibrium point in the array, where the sum of elements on the left of the index is equal to the sum of elements on the right of the index. If no equilibrium point exists, the function should return -1.

def equillibrium_points(arr):
    
    total_sum=sum(arr)
    left=0
    
    for i in range(len(arr)):
        
        right_sum = total_sum - left - arr[i]

        if left == right_sum :
            
            return i
        
        left += arr[i]


arr = [1, 3, 5, 2, 2]
print(equillibrium_points(arr))