# kth smallest element from the array

def kth_smallest_element(arr,k):
    
    def quick_sort(arr):
        
        if len(arr) <=1 :
            
            return arr
        
        else:
            
            mid=arr[len(arr)//2]
            left=[ x for x in arr if x < mid]
            middle=[x for x in arr if x== mid]
            right=[ x for x in arr if x > mid]

            return quick_sort(left) + middle + quick_sort(right)

    
    temp_sort = quick_sort(arr)

    return temp_sort[k-1]

arr=[4,1,3,6,7,2]
k=2

print(kth_smallest_element(arr,k))