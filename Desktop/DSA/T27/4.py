# You are given two arrays 'A' and 'B' of size 'N' and 'M' respectively. Both these arrays are sorted in non-decreasing order. You have to find the intersection of these two arrays.

# Intersection of two arrays is an array that consists of all the common elements occurring in both arrays.

# Note :
# 1. The length of each array is greater than zero.
# 2. Both the arrays are sorted in non-decreasing order.
# 3. The output should be in the order of elements that occur in the original arrays.
# 4. If there is no intersection present then return an empty array.

def intersect_of_two_sorted_array(a,b):
    
    i=j=0
    
    result=[]

    while i<len(a) and j<len(b):
        
        if a[i] == b[j]:
            
            result.append(a[i])

            i += 1
            j += 1
            
        elif a[i] < b[j]:
            
            i += 1
            
        else:
            
            j += 1
            
    
    return result

A = [1, 2, 3, 4, 5]
B = [3, 4, 5, 6, 7]

print(intersect_of_two_sorted_array(A,B))