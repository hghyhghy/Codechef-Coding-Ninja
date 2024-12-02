
#get occurance of a char 

def main(array,x):
    
    freq={}
    
    for num in array:
        
        if num in freq:
            
            freq[num] +=1 
            
        else:
            
            freq[num] = 1
    
    if x in freq:
        
        return freq.get(x,0)
    
n=int(input("enter"))
array=list(map(int,input().split()))

print(main(array,n))