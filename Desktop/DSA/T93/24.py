#lenght of longest subarray

def main(array):
    
    n=len(array)
    maximum=float("-inf")

    def continous(array):
        
        array.sort()
        
        n=len(array)
        for i in range(1,n):
            
            if array[i]-array[i-1] != 1:
                
                return False
            
        
        return True
    
    for i in range(n):
        
        for j in range(i,n):
            
            substring=array[i:j+1]
            
            if continous(substring):
                
                maximum=max(maximum,len(substring))
                
    return maximum

arr = [1, 2, 4]
print(main(arr))