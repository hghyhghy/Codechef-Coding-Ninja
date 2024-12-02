# Problem statement
# You are given an array consisting of 'N' positive integers where each integer is either 0 or 1 or 2. Your task is to sort the given array in non-decreasing order.

# Note :
# 1. The array consists of only 3 distinct integers 0, 1, 2.
# 2. The array is non-empty.

def sorting(array):
    
    def quick_sort(array):
        
        if len(array) <= 1:
            
            return array
        
        else:
            
            mid=array[len(array)//2]
            left=[x for x in array if x < mid]
            middle=[x for x in array if x == mid]
            right=[x for x in array if x > mid]
            
            return quick_sort(left)+middle+quick_sort(right)
        
    return quick_sort(array)
        
a=[2, 0, 1, 0, 2]
print(sorting(a))