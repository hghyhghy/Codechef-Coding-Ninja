

#sum of the two arrays 

def main(arr1,arr2):
    
    n=len(arr1)

    result=[0]*n
    
    for  i in range(n):
        
        result[i]= arr1[i] + arr2[i]

    return result

arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]

print(main(arr1,arr2))