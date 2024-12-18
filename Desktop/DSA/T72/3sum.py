# You are given an array/list ARR consisting of N integers. Your task is to find all the distinct triplets present in the array which adds up to a given number K.

# An array is said to have a triplet {ARR[i], ARR[j], ARR[k]} with sum = 'K' if there exists three indices i, j and k such that i!=j, j!=k and i!=j and ARR[i] + ARR[j] + ARR[k] = 'K'.

# Note:
# 1. You can return the list of values in any order. For example, if a valid triplet is {1, 2, -3}, then {2, -3, 1}, {-3, 2, 1} etc is also valid triplet. Also, the ordering of different triplets can be random i.e if there are more than one valid triplets, you can return them in any order.
# 2. The elements in the array need not be distinct.
# 3. If no such triplet is present in the array, then return an empty list, and the output printed for such a test case will be "-1".

def three_sum(array:list[int],target:int)->list[list]:
    
    result=set()
    n=len(array)
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            for k in range(j+1,n):
                
                total= array[i] +array[j]+array[k]
                
                if total == target:
                    
                   triplet = tuple(sorted([array[i],array[j],array[k]]))
                   result.add(triplet)
                   
    if result:
        
        return [list(triplet) for triplet in result]
    
    else:
        
        result -1
                    
                    
    return result

arr = [-1, 0, 1, 2, -1, -4]
print(three_sum(arr,0))