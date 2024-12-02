

#minimum chocolate distribution 

def main(array,m):

    n=len(array)
    array.sort()

    max_diff=float("inf")

    for i in range(n-m+1):
        
        diff=array[i+m-1]-array[i]

        if diff < max_diff:
            
            max_diff=diff
            
    
    return max_diff


chocolates = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
M = 7

print(main(chocolates,M))  