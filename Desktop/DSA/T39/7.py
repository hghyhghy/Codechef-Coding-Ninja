# Problem statement
# You are given two arrays of integers. Let's call the first array A and the second array B. A finds the number of elements in array B that are smaller than or equal to that element for every array element.

def smallest_element_from_the_two_array(array1,array2):
    
    result=[]

    for a in array1:
        
        count = 0
        
        for b in array2:
            
            if b <= a:
                
                count += 1
                
                result.append(b)

    return result

A = [3, 5, 7]
B = [1, 2, 3, 4, 5, 6]

print(smallest_element_from_the_two_array(A,B))