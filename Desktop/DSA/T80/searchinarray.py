# You are given two arrays ‘arr’ of size ‘n’ and ‘queries’ of size ‘q’. For each element ‘q’ in the array 'queries', your task is to find the sum of all elements in the array ‘arr’ which are less than or equal to ‘q’.

# For example: given array ‘arr = { 1, 2, 3, 3, 4, 5, 6, 7, 9, 10}’ and ‘ queries= { 3, 5}’ Then the sum of all elements whose value is less than or equal to ‘queries[0] = 3’ is ‘ 1+2+3+3 =9’. ‘queries[1] = 5’ is ‘1+2+3+3+4+5 =18’.
# You have to return the answer of every query { 9, 18}.

def sum_less_and_queries(array:list[int],queary:list[int])->int:
    
    result=[]
    
    for q in queary:
        current = 0
        
        for num in array:
            
            if num <= q:
                
                current += num
        
        result.append(current)
        
    
    return result

arr = [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]
queries = [3, 5]
print(sum_less_and_queries(arr,queries))