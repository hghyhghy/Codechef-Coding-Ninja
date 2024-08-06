# 3 Sum : Find triplets that add up to a zero


# 104

# 1
# Problem Statement: Given an array of N integers, your task is to find unique triplets that add up to give a sum of zero. In short, you need to return an array of all the unique triplets [arr[a], arr[b], arr[c]] such that i!=j, j!=k, k!=i, and their sum is equal to zero.

def three_sum_upto_zero(arr):
    
    n= len(arr)
    store=[]
    for i in range(n):
        
        for j in range(i+1,n):
            
            for k in range(j+1,n):
                
                if  arr[i] + arr[j] + arr[k] == 0:
                    
                    store.append([arr[i],arr[j],arr[k]])

    return store

nums = [-1,0,1,2,-1,-4]
print(three_sum_upto_zero(nums))

