# You are given an array consisting of 'N' positive integers where each integer is either 0 or 1 or 2. Your task is to sort the given array in non-decreasing order.

# Note :
# 1. The array consists of only 3 distinct integers 0, 1, 2.
# 2. The array is non-empty.

def quick_sort(array):
    
    def main(arr):
        
        if len(arr) <=1:
            
            return arr
        
        else:
            
            mid=arr[len(arr)//2]
            left=[x for x in arr if x<mid]
            middle=[x for x in arr if x==mid]
            right=[x for x in arr if x>mid]

            return main(left)+middle+main(right)

    return main(array)

a=[2 ,0 ,1 ,0 ,2]
print(quick_sort(a))