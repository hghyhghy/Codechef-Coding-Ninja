# You are given an array of integers 'ARR' containing N elements. Each integer is in the range [1, N-1], with exactly one element repeated in the array.

# Your task is to find the duplicate element. The duplicate element may be repeated more than twice in the error, but there will be exactly one element that is repeated in the array.

# Note :

# All the integers in the array appear only once except for precisely one integer which appears two or more times.

def finding_the_duplicates(arr):
    
    freq={}
    
    for num in arr:
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] = 1
            
    for num,count in freq.items():
        
        if count > 1:
            
            return num
        
    
    return None

arr = [1, 2, 3, 4, 5, 6, 7, 3]
print(finding_the_duplicates(arr))
    
    