
#move zero to end
def main(array):
    
    n=len(array)
    non_zero=0
    
    for i in range(n):
        
        if array[i]  != 0:
            
            array[non_zero],array[i]=array[i],array[non_zero]
            
            non_zero += 1
        
    return array

a=list(map(int,input().split()))
print(main(a))
