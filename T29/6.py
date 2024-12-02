# Problem statement
# You are given an unsorted array containing ‘N’ integers. You need to find ‘K’ largest elements from the given array. Also, you need to return the elements in non-decreasing order.

def kt_largest_element_in_arry(arr,k):
    
    def quick_sort(arr):
        
        if len(arr) <= 1:
            
            return arr
        
        else:
            
            mid=arr[len(arr)//2]
            left=[x for x in arr if x > mid]
            middle=[x for x in arr if x == mid]
            right=[x for x in arr if x < mid]

            return quick_sort(left) + middle + quick_sort(right)

    
    temp_store=quick_sort(arr)

    return temp_store[k-1]

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
K = 2

print(kt_largest_element_in_arry(arr,K))