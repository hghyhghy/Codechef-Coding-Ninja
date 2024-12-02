

#max_element at k distance 

def main(array,k):
    
    n=len(array)
    r=[]

    for i in range(n-k+1):
        
        maximum = array[i]

        for j in  range(i,i+k):
            
            if array[j] > maximum:
                
                maximum =  array[j]

        r.append(maximum)

    
    return r

arr = [3, 4, -1, 1, 5]
k = 3

print(main(arr,k))