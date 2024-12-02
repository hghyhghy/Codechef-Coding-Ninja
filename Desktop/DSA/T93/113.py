
#contigous array

def main(array:list[int])->int:
    
    n=len(array)
    max_len=float("-inf")
    
    for start in range(n):
        
        zero=0
        one=0
        
        for end in range(start,n):
            
            if array[end] ==0:
                
                zero +=1
                
            else:
                
                one +=1
                
            
            if zero == one:
                
                max_len=max(max_len,end-start+1)
                
    return max_len if max_len != float("-inf") else -1

arr=list(map(int,input().split()))
print(main(arr))