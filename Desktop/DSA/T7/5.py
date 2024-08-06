# Find the Largest element in an array


def finding_largest(arr):
    
    def quick_sort(arr):
        
        if len(arr) <= 1:
            
            return arr
        
        else:
            
            mid=arr[len(arr)//2]
            left = [x for x in arr if x > mid]
            middle=[x for x in arr if x == mid]
            right=[x for x in arr if x < mid]

            return quick_sort(left) + middle + quick_sort(right)

    
    temp_sort= quick_sort(arr)
    return temp_sort[0]

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(finding_largest(arr))
        