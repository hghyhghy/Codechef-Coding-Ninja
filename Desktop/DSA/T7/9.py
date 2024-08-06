# Find the repeating and missing numbers

def repeating_missing_number(array):
    
    n=len(array)
    count={}
    repeating_number=None
    
    for num in array:
        
        if num in count:
            
            repeating_number = num
            break
        
        count[num] = 1
        
    missing_number=None
    
    for i in range(1,n+1):
        
        if i not in count:
            
            missing_number = i
            break
        
    return repeating_number,missing_number

arr = [1, 2, 3, 3, 5]
print(repeating_missing_number(arr))

