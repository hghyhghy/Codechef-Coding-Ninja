# Problem statement
# You have been given an array/list 'ARR' of integers. Your task is to find the second largest element present in the 'ARR'.

# Note:
# a) Duplicate elements may be present.

# b) If no such element is present return -1.
# Example:
# Input: Given a sequence of five numbers 2, 4, 5, 6, 8.

def second_largest_element(aray):
    
    def bubble_sort(arr):
        
        n=len(arr)
        for i in range(n):
            
            for j in range(0,n-i-1):
                
                if arr[j]< arr[j+1]:
                    
                    arr[j],arr[j+1]= arr[j+1],arr[j]
                    
        return arr

    
    temporary = bubble_sort(aray)

    return temporary[1]

a= [2, 4, 5, 6, 8]
print(second_largest_element(a))