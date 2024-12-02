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


def kth_largest_element(arr):
    
    if len(arr) <=1:
        
        return arr
    
    else:
        
        mid=arr[len(arr)//2]
        left=[x for x in arr if x > mid]
        middle=[x for x in arr if x == mid ]
        right=[x for x in arr if x  < mid]

        return kth_largest_element(left) + middle  + kth_largest_element(right)
    

def main(arr,k):
    
    sort=kth_largest_element(arr)

    return sort[k-1]


a=[5,67,2,1,90,33]
k=2
print(main(a,k))