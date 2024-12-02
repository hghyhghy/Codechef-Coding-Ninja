#combination sum

from itertools import permutations

def main(array:list[int],target:int)->list[list[int]]:
    
    n=len(array)
    array.sort()
    new=set()
    
    for i in range(1,n+1):
        
        for perm in permutations(array,i):
            
            if sum(perm) == target:
                
                seen=tuple(sorted(perm))

                new.add(seen)

    
    r=list(sorted(new))
    return r

arr = [1,2,3,1]
target = 5
print(main(arr,target))