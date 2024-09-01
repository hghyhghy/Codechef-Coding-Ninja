# sum of the odd even indexed elemnts in the array

def sum_of_odd_even_indexed_elements(array):
    
    even=0
    odd=0
    
    for i in range(len(array)):
        
        if i %2 == 0:
            
            even += array[i]

        else:
            
            odd += array[i]

    
    return even,odd

arr = [1, 2, 3, 4, 5, 6]
print(sum_of_odd_even_indexed_elements(arr))