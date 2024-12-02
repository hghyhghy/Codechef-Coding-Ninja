# Problem statement
# You are given an array of integers 'ARR' of length 'N' and an integer Target. Your task is to return all pairs of elements such that they add up to Target.

# Note:

# We cannot use the element at a given index twice.
# Follow Up:

# # Try to do this problem in O(N) time complexity

def two_sum_pair_target(array,target):
    
    seen=set()
    pairs=[]

    for num  in array:
        
        complement=  target - num
        
        if complement in seen:
            
            pairs.append((num,complement))

        seen.add(num)
        
    final=[]
    
    for i in range(len(pairs)):
        
        if pairs[i] != pairs[i-1]:
            
            final.append(pairs[i])
    
    return final

arr = [1, 2, 3, 4, 3, 5, -1]
target = 4

print(two_sum_pair_target(arr,target))