

#difference equal to k 

def main(array,k):
    
    n=len(array)
    r=[]

    for i in range(n):
        
        for j in range(i+1,n):
            
            if abs(array[i]-array[j]) == k:
                
                r.append([array[i],array[j]])

    return r

arr = [1, 5, 3, 4, 2]
K = 2
print(main(arr,K))