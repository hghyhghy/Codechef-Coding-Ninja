# Find Second Smallest and Second Largest Element in an array

def second_largest_without_sorting(arr):
    
    largest=arr[0]
    n=len(arr)

    for i in range(n):
        
        if arr[i] > largest:
            
            largest = arr[i]
            
    second_largest=[]
    for j in range(n):
        
        if arr[j] < largest:
            
            second_largest.append(arr[j])

            
            
    return max(second_largest)

arr = [10, 5, 3, 8, 15, 12]
print(second_largest_without_sorting(arr))