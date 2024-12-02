# remove the consecutive duplicated from the array

def remove_consecutive_duplicates(array):
    
    n=len(array)

    dp=[]
    
    for i in range(n):
        
        if array[i] != array[i-1]:
            
            dp.append(array[i])

    return dp

arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
print(remove_consecutive_duplicates(arr))