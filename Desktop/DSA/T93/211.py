
#max consecutive one

def main(array):
    
    n=len(array)
    max_count=float("-inf")

    for i in range(n):
        
        count =0
        
        for j in range(i,n):
            
            if array[j] == 1:
                
                count +=1
                max_count=max(max_count,count)

            
            else:
                
                break
            
    return max_count

arr = [1, 1, 0, 1, 1, 1, 0, 1, 1]
print(main(arr))