# Find the duplicate in an array of N+1 integers

def finding_duplicate(arr):
    
    count={}

    for num in arr:
        
        if num in count:
            
            count[num] += 1
            
        else:
            
            count[num] = 1
            
            
    store=[]
    for val,count in count.items():
        
        if count > 1:
            
            store.append(val)

    
    return store

nums = [1, 3, 4, 2, 2]
print(finding_duplicate(nums))