# Problem statement
# Given an array arr of size N containing positive and negative integers. Arrange the array alternatively such that every non-negative integer is followed by a negative integer and vice-versa.

# Note:
# The number of positive integers and negative integers may not be equal. In such cases, add the extra integers at the end.
# For Example:
# For array {4, -9, -2, 6, -8}, the output will be {-9, 4, -2, 6, -8}

# For array {1, 2, 3, -5}, the output will be {-5, 1, 2, 3}   

def arrange_alternatively(array:list[int])->list[int]:
    
    positive=[x for x in array if x>=0]
    negative=[x for x in array if x<0]
    
    i=0
    j=0
    result=[]

    while i<len(positive) and j<len(negative):
        
        result.append(negative[j])
        result.append(positive[i])
        
        i+=1
        j+=1
    
    if j<len(negative):
        
        result.append(negative[j])
        i+=1
        
    if i<len(positive):
        
        result.append(positive[i])
        i+=1
        
  
    return result

print(arrange_alternatively([4, -9, -2, 6, -8]))
