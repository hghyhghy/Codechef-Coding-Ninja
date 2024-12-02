# You are given an array consisting of 'N' elements and you need to perform 'Q' queries on the given array. Each query consists of an integer which tells the number of elements by which you need to left rotate the given array. For each query return the final array obtained after performing the left rotations.

# Note:

# Perform each query on the original array only i.e. every output should be according to the original order of elements.
# Example:

# Let the array be [1, 2, 3, 4, 5, 6] and the queries be {2, 4, 1}. For every query, we’ll perform the required number of left rotations on the array.

# For the first query, rotate the given array to the left by 2 elements, so the resultant array is: [3, 4, 5, 6, 1, 2].

# For the second query, rotate the given array to the left by 4 elements, so the resultant array is: [5, 6, 1, 2, 3, 4].

# For the third query, rotate the give

def main_function(arr,d):
    
    n=len(arr)
    
    return arr[d%n:]+arr[:d%n]

def rotate_left(array,quaries):
    
    result=[]
    
    for queary in quaries :
        
        new_array = main_function(array,queary)
        
        result.append(new_array)
        
    return result

arr = [1, 2, 3, 4, 5, 6]
queries = [2, 4, 1]

# Process the queries and print results
output = rotate_left(arr, queries)
for res in output:
    print(res) 