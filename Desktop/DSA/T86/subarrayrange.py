# Problem statement
# Anish is teaching his brother about sub-arrays. However, his brother is sometimes very inattentive. So, he wants to test whether his brother has understood the concept of sub-arrays or not. He gives his brother two numbers and asks him to find the number of sub-arrays of a certain array ARR such that the maximum element of the sub-array lies between X and Y.

def subarray_lies_in_range(array:list[int],x:int,y:int)->int:
    
    n=len(array)
    count = 0
    
    for start in range(n):
        
        max_element = array[start]
        
        for end in range(start,n):
            
            max_element=  max(max_element,array[end])
            
            if x<=max_element<=y:
                
                count += 1
                
    return count

arr = [1, 2, 3, 4, 5]
X = 2
Y = 4
print(subarray_lies_in_range(arr, X, Y)) 