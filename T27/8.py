# You are given an array “ARR” of size N. Your task is to find out the sum of maximum and minimum elements in the array.

def sum_of_max_min(arr):
    
    def quick_sort(arr):
        
        if len(arr) <=1:
            
            return arr
        
        else:
            
            mid=arr[len(arr)//2]
            left=[x for x in arr if x < mid]
            middle=[x for x in arr if x == mid]
            right =[x for x in arr if  x> mid]

            return quick_sort(left) + middle + quick_sort(right)

    
    temp_sort=quick_sort(arr)

    return temp_sort[0]+temp_sort[len(temp_sort)-1]

arr = [3, 5, 1, 9, 2]
print(sum_of_max_min(arr))