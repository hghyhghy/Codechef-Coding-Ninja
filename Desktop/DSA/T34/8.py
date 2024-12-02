# Problem statement
# You are given an array/list ‘ARR’ consisting of ‘N’ distinct integers arranged in ascending order. You are also given an integer ‘TARGET’. Your task is to count all the distinct pairs in ‘ARR’ such that their sum is equal to ‘TARGET’.

# Note:

# 1. Pair (x,y) and Pair(y,x) are considered as the same pair. 

# 2. If there exists no such pair with sum equals to 'TARGET', then return -1.
# Example:

# Let ‘ARR’ = [1 2 3] and ‘TARGET’ = 4. Then, there exists only one pair in ‘ARR’ with a sum of 4 which is (1, 3). (1, 3) and (3, 1) are counted as only one pair

def pair_sum_target(arr,target):
    
    n=len(arr)
    count = 0
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            if arr[i] + arr[j] == target:
                
                count += 1
                
    return count

arr = [1, 2, 3, 4, 5, 6, 7]
target = 8

print(pair_sum_target(arr,target))