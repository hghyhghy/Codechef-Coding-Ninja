

def main(array):
    
    n=len(array)

    first=array[0]

    for i in range(n):
        
        array[i-1] = array[i]

    
    array[-1]= first
    
    return array

arr = [1, 2, 3, 4, 5]
print(main(arr))