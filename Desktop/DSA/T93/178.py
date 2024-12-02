

#rotate array

def main(array,x):
    
    n=len(array)
    x=x%n
    
    rotated= array[x:]+array[:x]

    return rotated

arr = [1, 2, 3, 4, 5, 6, 7]
x = 3

print(main(arr,x))