# Problem statement
# You are given an unsorted array containing ‘N’ integers. You need to find ‘K’ largest elements from the given array. Also, you need to return the elements in non-decreasing order.


def  kth_largest_element(array,k):
    
    def quick_sort(arr):
        
        if len(arr) <= 1:
            
            return arr
        
        else:
            
            mid=arr[len(arr)//2]
            left=[x for x  in arr if x > mid]
            middle=[x for x in arr if x == mid]
            right=[x for x in arr if x < mid]

            return quick_sort(left)+middle+quick_sort(right)
    
    temp = quick_sort(array)

    return temp[k-1]

a=[55,2,1,77,89,0,10]
print(kth_largest_element(a,2))
    
    