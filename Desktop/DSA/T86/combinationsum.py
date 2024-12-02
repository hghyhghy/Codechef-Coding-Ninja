# You are given an array ‘arr’ of ‘n’ positive integers.



# You are also given a positive integer ‘target’.



# Your task is to find all unique combinations of elements of array ‘arr’ whose sum is equal to ‘target’. Each number in ‘arr’ may only be used once in the combination.



# Elements in each combination must be in non-decreasing order and you need to print all unique combinations in lexicographical order.



# Note:
# In lexicographical order, combination/array  ‘a’  comes before array ‘b’ if at the first index 'i' where 'a[i]' differs from 'b[i]', 'a[i]' < 'b[i]  or length of 'a' is less than 'b'.

from itertools import permutations

def combination_sum(array:list[int],target:int)->list[list[int]]:
    
    n=len(array)
    array.sort()
    new=set()
    
    for i in range(1,n+1):
        
        for perm in permutations(array,i):
        #for lenght i ,2,3 as i++ or i increases 
        
            if sum(perm) == target:
                
                seen=tuple(sorted(perm))
                new.add(seen)

    
    r= list(sorted(new))
    return r

arr = [1,2,3,1]
target = 5
print(combination_sum(arr,target))

