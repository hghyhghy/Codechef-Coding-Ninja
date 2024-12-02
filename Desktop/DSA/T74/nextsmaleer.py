# You are given an array 'ARR' of integers of length N. Your task is to find the next smaller element for each of the array elements.

# Next Smaller Element for an array element is the first element to the right of that element which has a value strictly smaller than that element.

# If for any array element the next smaller element does not exist, you should print -1 for that array element.

# For Example:

# If the given array is [ 2, 3, 1], we need to return [1, 1, -1]. Because for  2, 1 is the Next Smaller element. For 3, 1 is the Next Smaller element and for 1, there is no next smaller element hence the answer for this element is -1.

def next_smaller_element(array:list[int])->list[int]:
    
    n=len(array)
    dp =[-1]*n
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            if array[j]< array[i]:
                
                dp[i] =  array[j]
                break
            
    return dp

arr = [4, 5, 2, 10, 8]
print(next_smaller_element(arr))