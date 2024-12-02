


#delete the k elements from the array 

def main(array,k):
    
    n=len(array)
    if k>= n:
        
        return array

    for i in range(k+1,n+1):
        
        print(array[i-1])


arr = [1, 3, 5, 7, 9]
K = 2

print(main(arr,K))
