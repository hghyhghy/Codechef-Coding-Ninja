# largets elenment in the array

def largest(arr):
    
    def quick_sort(arr):
        
        if len(arr) <= 1:
            
            return arr
        
        else:
            
            mid=arr[len(arr)//2]
            left=[x for x in arr if x > mid]
            middle=[x for x in arr if x==mid]
            right=[x for x in arr if x < mid]

            return quick_sort(left)+middle+quick_sort(right)

    temporary=quick_sort(arr)

    return temporary[0]

a=[1, 2, 3, 4, 5]
print(largest(a))