# Problem statement
# You are given an integer array 'ARR' of size ‘N’ and two integers ‘A’ and ‘B’. You need to find if there are two distinct indices in the array, such that the absolute difference of values on those indices is less than or equal to ‘B’ and the absolute difference of the indices is less than or equal to ‘A’.

# Note :
# Can you try to solve it in O(N) time ?

def find_indices(array:list[int],a:int,b:int)->bool:
    
    n=len(array)

    for i in range(n):
        
        for j in range(i+1,n):
            
            if abs(array[i]-array[j]) <=b and  abs(i-j)<=a:
                
                return True
            
    return False

ARR = [1, 5, 9, 1, 5, 9]
N = len(ARR)
A = 2
B = 3
print(find_indices(ARR,A,B))