# Find the duplicate in an array of N+1 integers

def finding_duplicate(array):
    
    seen={}

    for num in array:
        
        if num in seen:
            
            return num
        
        else:
            
            seen[num] =  True
            
            
arr = [1, 3, 4, 2, 2]
print(finding_duplicate(arr))

    