# Problem statement
# You are given an unsorted array containing ‘N’ integers. You need to find ‘K’ largest elements from the given array. Also, you need to return the elements in non-decreasing order.

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= T <= 100
# 1 <= N <= 10^4  
# 1<= K <= N  
# -10^9 <= ARR[i] <= 10^9

# Where ‘T’ is the number of test cases, ‘N’ is the size of the array, ‘K’ is the number of elements you need to return as an answer and ARR[i] is the size of the array of elements.

def main(arr,k):

    def quick_sort(arr):

       if len(arr) <= 1:

        return arr

       else:

        mid=arr[len(arr)//2]
        left=[x for x in arr if x > mid]
        middle=[x for x in arr if x == mid]
        right=[x for x in arr if x < mid]


        return quick_sort(left)+middle+quick_sort(right)
    temp=quick_sort(arr)
    new= temp[:k]
 
    return sorted(new)

a=[3,4,1,0,89,9]
k=2

print(main(a,k))
