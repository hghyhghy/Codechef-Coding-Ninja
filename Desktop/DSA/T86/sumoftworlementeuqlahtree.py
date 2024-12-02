# You are given an array Arr consisting of n integers, you need to find a valid triplet as explained below.

# An array is said to have a valid triplet {arr[i], arr[j], arr[k]} if there exists three indices i, j and k such that i != j, j != k and i != j and arr[i] + arr[j] = arr[k] or arr[i] + arr[k] = arr[j] or arr[k] + arr[j] = arr[i].

# For Example:
# Arr = 10, 5, 5, 6, 2, 
# In this array, the triplet {10, 5, 5} is valid triplet because, 5 + 5 = 10.

def triplet_sum(array:list[int])->list[int]:
    
    n=len(array)
    result=[]
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            for k in range(j+1,n):
                
                if i!=j and j!=k and i!= k:
                    
                    if array[i] + array[j] == array[k] or array[i]+array[k] == array[j] or array[j]+array[k] == array[i]:
                        
                        result.append([array[i],array[j],array[k]])

    return result

arr = [10, 5, 5, 6, 2]
print(triplet_sum(arr))