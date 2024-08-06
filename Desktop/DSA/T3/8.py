# Given an array arr of size n which contains elements in range from 0 to n-1, you need to find all the elements occurring more than once in the given array. Return the answer in ascending order. If no such element is found, return list containing [-1]. 

# Note: Try and perform all operations within the provided array. The extra (non-constant) ) space needs to be used only for the array to be returned.


def deleting_duplicates_from_array(array):
    
    seen={}
    temp=[]
    for num in array:
        
        if num in seen:
            
            seen[num] += 1
            
        else:
            
            seen[num] = 1
            
    for val,count in seen.items():
        
        if count > 1:
            
            temp.append(val)

    return temp

arr = [4, 3, 2, 7, 8, 2, 1, 5, 6, 1]
print(deleting_duplicates_from_array(arr))