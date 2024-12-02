# You are given an array Arr consisting of n integers, you need to find all the distinct triplets present in the array which adds up to zero.

# An array is said to have a triplet {arr[i], arr[j], arr[k]} with 0 sum if there exists three indices i, j and k such that i!=j, j!=k and i!=k and arr[i] + arr[j] + arr[k] = 0.

# Note :
# 1. You can return the list of values in any order. For example, if a valid triplet is {1, 2, -3}, then (2, -3, 1), (-3, 2, 1) etc is also valid triplet. Also, the ordering of different triplets can be random i.e if there are more than one valid triplets, you can return them in any order.
# 2. The elements in the array need not be distinct.
# 3. If no such triplet is present in the array, then return an empty list, and the output printed for such a test case will be "-1".

def triplet_sum_equal_to_zer(array):
    
    n=len(array)

    store=[]

    for i in range(n):
        
        for j in range(i+1,n):
            
            for k in range(j+1,n):
                
                if (array[i]+array[j]+array[k]) == 0:
                    
                    store.append([array[i],array[j],array[k]])

    return store

arr = [-1, 0, 1, 2, -1, -4]

print(triplet_sum_equal_to_zer(arr))