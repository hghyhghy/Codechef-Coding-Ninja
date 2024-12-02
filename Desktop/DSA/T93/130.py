

#finding duplicate

def main(array):
    
    n=len(array)
    result=[]

    for  i in range(1,n):
        
        if array[i] == array[i-1]:
            
            result.append(array[i])

    
    return result

nums=list(map(int,input().split()))
print(main(nums))