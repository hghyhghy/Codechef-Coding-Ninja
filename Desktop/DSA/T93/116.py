

#count pairs with sum

def main(array,target,x,y):
    
    n=len(array)
    count = 0
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            if (array[i]*x + array[j]*y) == target:
                
                count += 1
                
    return count

A = [1, 2, 3, 4, 5]
X = 2
Y = 3
SUM1 = 11

print(main(A,SUM1,X,Y))