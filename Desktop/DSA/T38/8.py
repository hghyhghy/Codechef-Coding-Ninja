# Problem statement
# Given an array of size N, containing N integers. Find out in what order should the elements be organized such that the function F(i) = a[i+1] ^ a[i] is maximum for 0 <= i <= N - 1.

def maximize_xor(arr):
    
    def quick_sort(arr):
        
        if len(arr) <= 1:
            
            return arr
        
        else:
            
            mid=arr[len(arr)//2]
            left=[x for x in arr if x > mid]
            middle=[x for x in arr if x ==mid]
            right=[x for x in arr if x<mid]

            return quick_sort(left)+middle+quick_sort(right)

    
    return quick_sort(arr)

arr = [3, 8, 2, 7, 6]
print(maximize_xor(arr))
