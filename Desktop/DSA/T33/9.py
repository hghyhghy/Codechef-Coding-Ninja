# Problem statement
# You are given an array ‘ARR’ containing ‘N’ integers.



# Return all the unique triplets [ARR[i], ARR[j], ARR[k]] such that i != j, j != k and k != i and their sum is equal to zero.



# Example:
# Input: ‘N’ = 5 
# 'ARR' =  [-1, -1, 2, 0, 1] 

def three_sum_brute_force(array):
    
    n=len(array)
    store=[]

    for i in range(n):
        
        for j in range(i+1,n):
            
            for k in range(j+1,n):
                
                if array[i]+array[j]+array[k] == 0:
                    
                    store.append([array[i],array[j],array[k]])

    return store

a=[-1, -1, 2, 0, 1] 
print(three_sum_brute_force(a))