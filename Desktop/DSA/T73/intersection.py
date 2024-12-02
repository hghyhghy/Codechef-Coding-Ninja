1# Problem statement
# You are given two arrays 'A' and 'B' of size 'N' and 'M' respectively. Both these arrays are sorted in non-decreasing order. You have to find the intersection of these two arrays.

# Intersection of two arrays is an array that consists of all the common elements occurring in both arrays.

# Note :
# 1. The length of each array is greater than zero.
# 2. Both the arrays are sorted in non-decreasing order.
# 3. The output should be in the order of elements that occur in the o

def intersection(arr1:list[int],n:int,arr2:list[int],m:int)->list[int]:
    
    i=0
    j=0
    result=[]
    
    while i<n  and j<m:
        
        if arr1[i] == arr2[j]:
            
            result.append(arr1[i])
            
            i +=1
            j +=1
            
        elif arr1[i] < arr2[j]:
            
            i +=1
            
        else:
            
            j += 1
            
    return result

arr = [1, 2, 4, 5, 6]
brr = [2, 3, 5, 7]
n = len(arr)
m = len(brr)

print(intersection(arr,n,brr,m))