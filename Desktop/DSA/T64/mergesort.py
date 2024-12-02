# Problem statement
# Given a sequence of numbers ‘ARR’. Your task is to return a sorted sequence of ‘ARR’ in non-descending order with help of the merge sort algorithm.

# Example :

# Merge Sort Algorithm -

# Merge sort is a Divide and Conquer based Algorithm. It divides the input array into two-parts, until the size of the input array is not ‘1’. In the return part, it will merge two sorted arrays a return a whole merged sorted array.

def merge_sort(string):
    
    n=len(string)
    if n <=1:
        
        return string
    
    mid=n//2
    
    left=merge_sort(string[:mid])
    right=merge_sort(string[mid:])
    
    return merge(left,right)
    
def merge(left,right):
    
    i=j=0
    result=[]

    while i<len(left) and j<len(right):
        
        if left[i]<=right[j]:

            result.append(left[i])

            i += 1
            
        else:
            
            result.append(right[j])

            j += 1
            
            
    result.extend(left[i:])
    result.extend(right[j:])

    return result

ARR = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(ARR))
            