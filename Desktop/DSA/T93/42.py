
#arrange positive or negative 
def main(array):
    
    pos=[]
    neg=[]

    for  num in array:
        
        if num < 0:
            
            neg.append(num)

        else:
            
            pos.append(num)

    i=0
    
    while pos and neg:
        
        array[i] =  pos.pop()
        i +=1
        
        array[i] = neg.pop()
        i+=1
        
    return array

arr=list(map(int,input().split()))
print(main(arr))
            
            