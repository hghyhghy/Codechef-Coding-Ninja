# You are given an array ‘Arr’ consisting of ‘N’ distinct integers and a positive integer ‘K’. Find out Kth smallest and Kth largest element of the array. It is guaranteed that K is not greater than the size of the array.

# Example:

# Let ‘N’ = 4,  ‘Arr’ be [1, 2, 5, 4] and ‘K’ = 3.  
# then the elements of this array in ascending order is [1, 2, 4, 5].  Clearly, the 3rd smallest and largest element of this array is 4 and 2 respectively.

def kth_largest_and_smallest(array:list,k:int)->int:
    
    largest=-1
    smallest=-1
    
    new_array=sorted(array)
    smallest=new_array[k-1]
    
    new_array1=sorted(array,reverse=True)
    largest= new_array1[k-1]
    
    return largest,smallest

a=[34,21,3,1,89]
k=2

print(kth_largest_and_smallest(a,k))