# To find all subarrays of an array that consist of distinct elements using a set and a two-for-loop approach, we can use a brute force method to generate all possible subarrays and then check if the elements in each subarray are distinct.

def subarray_with_distinct_elements(array):
    
    n=len(array)
    result = []

    for start in range(n):
        
        seen=set()

        for end in range(start,n):
            
            if array[end] in seen:
                
                break
            
            seen.add(array[end])
            result.append(array[start:end+1])

    return result

arr = [1, 2, 3, 2, 1]
print(subarray_with_distinct_elements(arr))