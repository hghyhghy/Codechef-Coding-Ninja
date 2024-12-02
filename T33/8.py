# You are given an array arr of length N. You have to return a list of integers containing the NGE(next greater element) of each element of the given array. The NGE for an element X is the first greater element on the right side of X in the array. Elements for which no greater element exists, consider the NGE as -1.

# For Example :

# If the given array is [1, 3, 2], then you need to return [3, -1, -1]. Because for 1, 3 is the next greater element, for 3 it does not have any greater number to its right, and similarly for 2.

def next_greater_element(array):
    
    n=len(array)
    dp=[-1]*n
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            if array[j] > array[i]:
                
                dp[i] = array[j]
                break
            
    return  dp 


arr = [1, 3, 2]

print(next_greater_element(arr))
