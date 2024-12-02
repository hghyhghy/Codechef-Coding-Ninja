

# 3 pair sum from an array 

def three_sum_pair(arr,target):

    if not arr:

        return 0
    
    temp_store=[]
    
    n=len(arr)
    
    for i in range(n):

        for j in range(i+1,n):

            for k in range(j+1,n):

                temp_sum= arr[i] + arr[j] + arr[k]

                if temp_sum ==  target:

                    temp_store.append([arr[i],arr[j],arr[k]])

    return temp_store

nums = [-1, 0, 1, 2, -1, -4]
target = 0

print(three_sum_pair(nums,target))

