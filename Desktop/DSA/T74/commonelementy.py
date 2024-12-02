# Problem statement
# You are given three arrays 'A', 'B' and 'C' of length 'N', 'M' and 'K' respectively. All the three arrays are sorted in non-decreasing order. Your task is to find all such elements which are present in all the three given arrays.

# Note:

# 1. The output array should have the same ordering of elements as the original arrays.
# 2. Even if a particular element appears more than once in each of the three arrays, it should still be present only once in the output array.
# 3. If there are no common elements in the arrays, return an empty array.
# For example:

# Consider the three arrays A = [ 2, 3, 4, 7 ] , B = [ 0, 0, 3, 5 ] , C = [ 1, 3, 8, 9 ]
# The output array should be [ 3 ] as 3 is the only element which is present in all the three arrays.

def common_elements(arr1:list[int],arr2:list[int],arr3:list[int])->list[int]:
    
    i=j=k=0
    reuslt=[]
    
    while i<len(arr1) and j <len(arr2) and k<len(arr3):
        
        if arr1[i] == arr2[j] == arr3[k]:
            
            if not reuslt or reuslt[-1] != arr1[i]:
                
                reuslt.append(arr1[i])
                
            i +=1
            j +=1
            k +=1
            
        elif arr1[i] < arr2[j]:
            
            i += 1

        elif arr2[j] < arr3[k]:
            
            j += 1
            
        else:
            
            k +=1
            
    return reuslt

A = [2, 3, 4, 7]
B = [0, 0, 3, 5]
C = [1, 3, 8, 9]

print(common_elements(A,B,C))