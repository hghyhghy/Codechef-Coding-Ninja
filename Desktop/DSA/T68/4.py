# Problem statement
# You are given an array of integers. You need to sort the array in ascending order using quick sort.

# Quick sort is a divide and conquer algorithm in which we choose a pivot point and partition the array into two parts i.e, left and right. The left part contains the numbers smaller than the pivot element and the right part contains the numbers larger than the pivot element. Then we recursively sort the left and right parts of the array.

# Example:

# Let the array = [ 4, 2, 1, 5, 3 ]
# Let pivot to be the rightmost number.

def main(array:list)->list:
    
    def quick_sort(arr:list)->list:
        
        if len(arr)<=1:
            
            return arr
        
        else:
            
            mid=arr[len(arr)//2]
            left=[x for x in arr if x<mid]
            middle=[x for x in arr if x==mid]
            right=[x for x in arr if x>mid]
            
            return quick_sort(left)+middle+quick_sort(right)

    temp =quick_sort(array)

    return temp

a=[78,3,45,1,0,4]
print(main(a))