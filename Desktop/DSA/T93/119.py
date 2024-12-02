

#finding duplicate

def main(array):
    
    freq={}
    
    for num in array:
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] = 1
            
            
    r=[num for num,count in freq.items() if count > 1]

    return r

arr=list(map(int,input().split()))
print(main(arr))