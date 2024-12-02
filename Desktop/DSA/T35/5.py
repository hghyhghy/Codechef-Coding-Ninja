# You are given an array of 'N' integers denoting the heights of the mountains. You need to find the length of the longest subarray which has the shape of a mountain.

# A mountain subarray is defined as a subarray which consists of elements that are initially in ascending order until a peak element is reached and beyond the peak element all other elements of the subarray are in decreasing order.

def longest_mountain_subarray(arr):
    
    n=len(arr)
    lenght= 0
    
    
    for  i in range(1,n-1):
        
        if arr[i-1] < arr[i] > arr[i+1]:
            
            left = i
            
            while left > 0 and arr[left-1] < arr[left]:
                
                left -= 1
                
            
            right = i
            
            while right < n-1 and arr[right] > arr[right+1]:
                
                right += 1
                
                
            current_lenght= right-left+1
            
            lenght = max(lenght,current_lenght)

    return lenght

arr = [2, 1, 4, 7, 3, 2, 5]
print(longest_mountain_subarray(arr))