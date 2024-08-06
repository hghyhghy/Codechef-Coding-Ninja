# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

def squares_of_the_sorted_array(array):
    
    def quick_sort(arr):
        
        if len(arr) <=1 :
            
            return arr
        
        else:
            
            mid=arr[len(arr)//2]
            left=[x for x in arr if  x<mid]
            middle=[x for x in arr if  x==mid]
            right=[x for x in arr if  x>mid]

            return quick_sort(left) + middle + quick_sort(right)

    
    temp_store = quick_sort(array)

    return sorted([ num *num for num in temp_store])

nums = [-4,-1,0,3,10]
print(squares_of_the_sorted_array(nums))
