# Problem statement
# You are given an array of ‘N’ distinct integers and an integer ‘X’ representing the target sum. You have to tell the minimum number of elements you have to take to reach the target sum ‘X’.

from  itertools import combinations

def minimum_number_to_find_target(array:list[int],x:int)->list[int]:
    
    n=len(array)
    min_count =float("inf")
    
    for i in range(1,n):
        
        for subset in combinations(array,i):
            
            temp =sum(subset)
            
            if temp == x:
                
                min_count=min(min_count,len(subset))
                
    return min_count if min_count != float('inf') else -1


arr = [1, 2, 3, 4, 5]
X = 9

print(minimum_number_to_find_target(arr,X))