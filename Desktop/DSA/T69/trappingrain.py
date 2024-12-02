# Problem statement
# You have been given a long type array/list 'arr’ of size 'n’.


# It represents an elevation map wherein 'arr[i]’ denotes the elevation of the 'ith' bar.


# Print the total amount of rainwater that can be trapped in these elevations.



# Note :
# The width of each bar is the same and is equal to 1.
# Example:
# Input: ‘n’ = 6, ‘arr’ = [3, 0, 0, 2, 0, 4].

def trapping_rain_water(array:list)->int:
    
    total_water  = 0
    n=len(array)
    
    for i in range(1,n-1):
        
        left=max(array[:i])
        right=max(array[i+1:])
        
        water = min(left,right) - array[i]
        
        if water > 0:
            
            total_water += water
            
    return total_water

arr = [3, 0, 0, 2, 0, 4]
print(trapping_rain_water(arr))