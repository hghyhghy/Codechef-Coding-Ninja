# You are given an array of integers 'ARR' containing N elements. Each integer is in the range [1, N-1], with exactly one element repeated in the array.

# Your task is to find the duplicate element. The duplicate element may be repeated more than twice in the error, but there will be exactly one element that is repeated in the array.

# Note :

# All the integers in the array appear only once except for precisely one integer which appears two or more times.

def finding_duplicate_in_the_array(array):
    
    result=[]
    n=len(array)

    for num in range(1,n):
        
        if array[num] == array[num-1]:
            
            result.append(array[num])

    return result

a=[1,1,2]
print(finding_duplicate_in_the_array(a))