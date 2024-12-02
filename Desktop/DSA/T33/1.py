# Problem statement
# You are given an array 'a' of size 'n'.



# Print the Next Greater Element(NGE) for every element.



# The Next Greater Element for an element 'x' is the first element on the right side of 'x' in the array, which is greater than 'x'.



# If no greater elements exist to the right of 'x', consider the next greater element as -1.

def next_gretaer_element(array):
    
    n=len(array)
    dp=[-1] * n
    
    for  i in range(n):
        
        dp[i] = -1
        
        for j in range(i+1,n):
            
            if array[j] > array[i]:
                
                dp[i] = dp[j]

                break
            
    for i in range(n):
        print(f"Next Greater Element for {arr[i]} is {dp[i]}")

arr = [4, 5, 2, 10, 8]

print(next_gretaer_element(arr))