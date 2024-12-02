# You have been given an array/list 'arr' consisting of 'n' elements.



# Each element in the array is either 0, 1 or 2.



# Sort this array/list in increasing order.



# Do not make a new array/list. Make changes in the given array/list.

def sort_array_list(array):
    
    
    def quick_sort(arr):
        
        if len(arr) <=1:
            
            return arr
        
        else:
            
            mid=arr[len(arr)//2] 
            left=[x for x in arr if x < mid]
            middle=[x for x in arr if x == mid]
            right=[ x for x in arr if x>mid]

            return quick_sort(left)+middle+quick_sort(right)

    temporary= quick_sort(array)

    return temporary

a=[2, 2, 2, 2, 0, 0, 1, 0]
print(*sort_array_list(a))