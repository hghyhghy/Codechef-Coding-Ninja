# You are given an array/list 'ARR' of ‘N’ integers and an integer value ‘TARGET’. You need to check whether there exist four numbers (ARR[i], ARR[j], ARR[k], ARR[l]) such that (0 <= i < j < k < l < N) and ARR[i] + ARR[j] + ARR[k] + ARR[l] = 'TARGET'.

# Note:
# 1. All four numbers should exist at different indices in the given array.
# 2. The answer is case-sensitive.

def foursum(array:list[int],target:int)->list[int]:
    
    n=len(array)
    seen=set()
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            for k in range(j+1,n):
                
                for l in range(k+1,n):
                    
                    if array[i]+array[j]+array[k]+array[l] == target:
                        
                        seen.add(tuple(sorted([array[i],array[j],array[k],array[l]])))

    
    return list(seen) if seen else -1

arr = [1, 0, -1, 0, -2, 2]
N = len(arr)
target = 0
print(foursum(arr,target))