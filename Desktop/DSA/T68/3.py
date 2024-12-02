# You are given an array 'a' of size 'n'.



# Print the Next Greater Element(NGE) for every element.



# The Next Greater Element for an element 'x' is the first element on the right side of 'x' in the array, which is greater than 'x'.



# If no greater elements exist to the right of 'x', consider the next greater element as -1.


def next_greater_element(array:list)->list:
    
    n=len(array)
    dp=[-1]*n
    
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            if array[j] > array[i]:
                
                dp[i] = array[j]
                break
    
    return dp

arr = [4, 5, 2, 25]
print(next_greater_element(arr))