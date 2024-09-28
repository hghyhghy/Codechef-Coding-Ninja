# Problem statement
# Given an array 'ARR'' of 'N' integers and an integer 'target', your task is to find three integers in 'ARR' such that the sum is closest to the target.

# Note
# In the case of two closest sums, print the smallest sum.

def three_sum_closest(array,target):
    
    n=len(array)
    close_sum=float('inf')

    for i in range(n):
        
        for j in range(i+1,n):
            
            for k in range(j+1,n):
                
                current = array[i]+array[j]+array[k]

                if abs(current-target) < abs(close_sum-target):
                    
                    close_sum=current
                    
    return close_sum

arr = [-1, 2, 1, -4]
target = 1
print(three_sum_closest(arr,target))