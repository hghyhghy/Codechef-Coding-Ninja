# Problem statement
# You have been given an array/list ‘ARR’ consisting of ‘N’ positive integers. Your task is to return the Next Greater Element(NGE) for every element.

# The Next Greater Element for an element ‘X’ is the first element on the right side of ‘X’ in the array 'ARR', which is greater than ‘X’. If no such element exists to the right of ‘X’, then return -1.

# For example:
# For the given array 'ARR' = [7, 12, 1, 20]

# The next greater element for 7 is 12.
# The next greater element for 12 is 20. 
# The next greater element for 1 is 20. 
# There is no greater element for 20 on the right side.

# So, the output is [12, 20, 20, -1].

def next_greater_element(array):
    
    n=len(array)
    dp=[-1]*n

    for i in range(n):
        
        for j in range(i+1,n):
            
            if array[j] > array[i]:
                
                dp[i]=array[j]

                break
    
    return dp

arr = [4, 5, 2, 25, 7, 8]
print(next_greater_element(arr))