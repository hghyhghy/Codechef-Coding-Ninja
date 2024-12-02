# Problem statement
# You are given an array ‘arr’ that contains an equal number of positive and negative elements. Rearrange the given array such that positive and negative numbers are arranged alternatively. Also, the respective relative order of positive and negative should be maintained.

# For example:

# For the given arr[ ] = { -1, 3, 5, 0, -2, -5 } 
# arr[ ] = {3, -1, 5, -2, 0, -5 } is valid rearrangement.
# arr[ ] = {3, -1, 0, -2, 5, -5 } is invalid rearrangement; order of 0 and 5 is changed. 
# arr[ ] = {3, -1, 5, 0, -2, -5 } is invalid rearrangement; positive and negative elements are not alternative.
# Note:

# Make changes in the same array and no returning or printing is needed.
# Consider zero(0) as a positive element for this question.
# It is guaranteed that an answer always exists.

def arrange_positive_negative(array:list[int])->list[int]:
    
    pos=[]
    neg=[]

    for num in array:
        
        if num > 0:
            
            pos.append(num)

        else:
            
            neg.append(num)
            
    i=0
    
    while pos and neg:
        
        array[i] = pos.pop(0)
        
        i += 1
        
        array[i] =  neg.pop(0)

        i+=1
        
    
    return array

arr = [1, -1, 2, -2, 3, -3]
print(arrange_positive_negative(arr))