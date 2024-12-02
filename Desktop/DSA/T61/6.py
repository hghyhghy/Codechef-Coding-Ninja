# Problem statement
# You are given an array of integers 'ARR' containing N elements. Each integer is in the range [1, N-1], with exactly one element repeated in the array.

# Your task is to find the duplicate element. The duplicate element may be repeated more than twice in the error, but there will be exactly one element that is repeated in the array.

# Note :

# All the integers in the array appear only once except for precisely one integer which appears two or more times.

def find_duplicates(array):
    
    freq={}
    
    for num in array:
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] = 1
            
    result= [num for num,count in freq.items() if count > 1]

    return result

a=[1, 3, 4 ,2 ,2]
print(find_duplicates(a))