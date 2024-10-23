# You are given two sorted arrays of distinct integers, ‘ARR1’ and ‘ARR2’. If you find a common element in both arrays, you can switch from one array to another.

# Your task is to find a path through the intersections i.e common integers of ‘ARR1’ and ‘ARR2’, that produces maximum sum and return that maximum sum as the answer.

def maximum_of_intersection(arr1,arr2):
    
    common = list(set(arr1)&set(arr2))
    
    if len(common) < 2:
        
        return
    
    max_sum = float("-inf")
    max_pair=None
    
    n=len(common)
    for i in range(n):
        
        for j in range(i+1,n):
            
            current=common[i]+common[j]

            if current > max_sum:
                
                max_sum = current
                max_pair=(common[i],common[j])

        return max_sum,max_pair
    
    

    return common
arr1 = [1, 5, 3, 8, 12]
arr2 = [3, 8, 7, 10, 5]

print(maximum_of_intersection(arr1,arr2))