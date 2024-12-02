# You are given an array/list 'ARR' of ‘N’ integers and an integer value ‘TARGET’. You need to check whether there exist four numbers (ARR[i], ARR[j], ARR[k], ARR[l]) such that (0 <= i < j < k < l < N) and ARR[i] + ARR[j] + ARR[k] + ARR[l] = 'TARGET'.

def find_four_elements_sums_to_target(arr,x):
    
    arr.sort()
    n=len(arr)
    store=[]

    for i in range(n):
        
        for j in range(i+1,n):
            
            for k in range(j+1,n):
                
                for l in range(k+1,n):
                    
                    if arr[i]+arr[j]+arr[k]+arr[l] == x:
                        
                        store.append([arr[i],arr[j],arr[k],arr[l]])

    
    return store

nums = [1, 0, -1, 0, -2, 2]
target = 0

print(find_four_elements_sums_to_target(nums,target))