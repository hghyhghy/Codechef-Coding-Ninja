
# two sum 

def two_sum_brute_force(arr,target):

    temp_store=[]

    for i in range(0,len(arr)):

        for j in range(i+1,len(arr)):

            if arr[i] + arr[j] == target:

                temp_store.append([arr[i],arr[j]])

    
    return temp_store

nums = [2, 7, 11, 15]
target = 9

print(two_sum_brute_force(nums,target))