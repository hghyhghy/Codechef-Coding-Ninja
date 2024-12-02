# You have been given two integers 'A' and 'B' return minimum and maximum of both the numbers without branching.

# Note :
# Branching includes if-else statements, the ternary operator, or switch-case statements. Therefore you should not use any of the above approaches to solving the problem.

from typing import List,Tuple

def minimum_maximum(array:list[int]) -> Tuple[int,int]:
    
    if not array or len(array) == 1:
        
        return array
    
    minimum=array[0]
    maximum=array[0]

    for num in array:
        
        if num > maximum:
            
            maximum =  num
            
        if num < minimum:
            
            minimum = num
            
    return minimum,maximum

arr = [3, 5, 1, 9, 2, 8]
print(minimum_maximum(arr))