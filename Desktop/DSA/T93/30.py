#cyclically rotate array by one 
def main(array:list[int])->list[int]:
    
    n=len(array)
    last=array[-1]

    for i in range(n-1,-1,-1):
        
        array[i] = array[i-1]
        
    array[0]=last
    
    return array

a=list(map(int,input().split()))

print(main(a))