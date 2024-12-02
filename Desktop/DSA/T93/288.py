
#buy and sell stock 

def main(array):
    
    n=len(array)
    maximum=float("-inf")

    for i in range(n-1):
        
        if array[i+1] > array[i]:
            
            maximum +=  array[i+1] - array[i]

    
    return maximum

