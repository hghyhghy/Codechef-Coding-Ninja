# You are given an array of integers 'ARR' of length 'N' and an integer Target. Your task is to return all pairs of elements such that they add up to Target.

# Note:

# We cannot use the element at a given index twice.
# Follow Up:

def find_pair_with_target(arr,target):
    
    pairs=[]

    n=len(arr)

    for i in range(n):
        
        for j in range(i+1,n):
            
            if arr[i] + arr[j] == target:
                
                pairs.append([arr[i],arr[j]])

    return pairs

arr = [1, 2, 3, 4, 5]
target = 5

print(find_pair_with_target(arr,target))