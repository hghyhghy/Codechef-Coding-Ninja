# You are given a circular array 'a' of length 'n'.



# A circular array is an array in which we consider the first element is next of the last element. That is, the next element of 'a[n - 1]' is 'a[0]'.



# Find the Next Greater Element(NGE) for every element.



# The Next Greater Element for an element 'x' is the first element on the right side of 'x' in the array, which is greater than 'x'.



# If no greater elements exist to the right of 'x', consider the next greater element as -1.


def next_greater_element_circular_array(array:list[int])->list[int]:
    
    n=len(array)
    next_greater=[-1]*n
    
    for i in range(n):
        
        for j in range(1,n):
            
            next_element=(i+j)%n
            
            if array[next_element] > array[i]:
                
                next_greater[i] = array[next_element]
                break
    
    return next_greater

arr = [1, 5, 3, 4, 2]
print(next_greater_element_circular_array(arr))