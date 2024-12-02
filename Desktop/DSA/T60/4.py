# You have been given a sorted array/list 'arr' consisting of ‘n’ elements. You are also given an integer ‘k’.



# Now the array is rotated at some pivot point unknown to you.



# For example, if 'arr' = [ 1, 3, 5, 7, 8], then after rotating 'arr' at index 3, the array will be 'arr' = [7, 8, 1, 3, 5].



# Now, your task is to find the index at which ‘k’ is present in 'arr'.

def search_in_roated_sorted_array(array,target):
    
    n=len(array)
    left=0
    right=n-1
    
    while left<=right:
        
        mid=(left+right)//2
        
        if array[mid] == target:
            
            return mid
        
        if array[left]<=array[mid]:
            
            if array[left]<=target<array[mid]:
                
                right=mid-1
                
            else:
                
                left=mid+1
                
        else:
            
            if array[mid] < target<= array[right]:
                
                left=mid+1
                
            else:
                
                right=mid-1
                
    return -1

arr = [7, 8, 1, 3, 5]
k = 3

print(search_in_roated_sorted_array(arr,k))