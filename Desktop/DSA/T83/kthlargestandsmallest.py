# Problem statement
# Given an array and a number K where K is smaller than size of array, we need to find the K'th smallest element and K'th largest element in the given array. It is given that all array elements are not distinct.

# Note:
# If element is not present, then return -1.
# K'th largest and smallest element in the sorted array. You are given an array consisting of N non distinct positive integers and a number K, your task is to find the K'th largest and K'th smallest element in the array.
# 1) Kth largest and smallest element in an array is the K'th element of the array when sorted in increasing order. For example consider the array {2, 1, 5, 6, 3, 3, 8} and K=4, the sorted array will be {1, 2, 3, 3, 5, 6, 8}. But we will check the array {1, 2, 3, 5, 6, 8} as 3 is repeated twice and the 4th largest element will be 3 and 4th smallest will be 5.

# 2) All the elements of the array are not distinct.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= T <= 100
# 1 <= N <= 10^3
# 1 <= arr[i] <= 10^9
# 1 <= K < N
# Sample Input 1:
# 1
# 3 2
# 1 2 3
# Sample Output 1:
# 2 2
# Explanation for sample input 1:
# 2 is the second largest and second smallest element in an array {1,2,3}.
# Sample Input 2:
# 1
# 3 2
# 5 5 5
# Sample Output 2:
# -1 -1
# Explanation for sample input 2:
# Since there is only 1 unique element therefore second largest and second smallest element does not exist hence -1.

def kth_largest_smallest(array:list[int],k:int)->int:
    
    
    def quick_sort(array):
        
        if len(array)<=1:
            
            return array
        
        else:
            
            mid=array[len(array)//2]
            left=[ x for x in array if x>mid]
            middle=[x for x in array if x == mid]
            right=[ x for x in array if x<mid]
            
            return quick_sort(left)+ middle + quick_sort(right)
        
    new_arry=quick_sort(array)
    
    smallest=new_arry[k-1]
    
    
    new= sorted(array,reverse=True)
    
    largest =  new[k-1]
    
    return smallest,largest

arr = [2, 1, 5, 6, 3, 3, 8]
K = 4
print(kth_largest_smallest(arr,K))
        
    
    