# Kth largest element in an array [use priority queue]

def kth_largest_element_in_an_array(array,k):
    
    def quick_sort(arr):
        
        if len(arr) <=1 :
            
            return arr
        
        else:
            
            mid=arr[len(arr)//2]
            left=[x for x in arr if x > mid]
            middle=[x for x in arr if x == mid]
            right=[x for x in arr if x<mid]

            return quick_sort(left) + middle + quick_sort(right)

    
    stored=quick_sort(array)

    return stored[k-1]

arr = [3, 2, 1, 5, 6, 4]
k = 2

print(kth_largest_element_in_an_array(arr,k))