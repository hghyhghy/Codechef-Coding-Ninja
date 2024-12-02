# Problem statement
# You are given two arrays of integers. Let's call the first array A and the second array B. A finds the number of elements in array B that are smaller than or equal to that element for every array element.

from  bisect import  bisect_right

def equal_or_smaller_elements(a:list,b:list)->list:
    
    result=[]
    b.sort()

    for  A in a:
        
        count =  bisect_right(b,A)
        result.append(count)

    
    return result

A = [4, 5, 6]
B = [1, 2, 4, 4, 5]

print(equal_or_smaller_elements(A,B))

