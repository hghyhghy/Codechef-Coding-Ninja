# sort binary 0 1

def sorting_binary_zero_one(array):
    
    current = 0
    n=len(array)
    for i in range(n):
        
        if array[i] == 0:
            
            array[i],array[current] = array[current],array[i]

            current += 1
        
    return array

arr = [1, 0, 1, 0, 1, 0, 1, 0]
print(sorting_binary_zero_one(arr))