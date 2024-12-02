

#product of array less than  k 

def main(array,target):
    
    n=len(array)
    count = 0
    
    for i in range(n):
        
        product =1
        
        for j in range(i,n):
            
            product  *= array[j]
            
            if product < target:
                
                count += 1
                
            else:
                
                break
            
    return count

nums = [10, 5, 2, 6]
k = 100

