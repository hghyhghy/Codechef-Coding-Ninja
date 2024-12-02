

#single element in the sorted array 

def main(array):
    
    freq={}

    for num in array:
        
        if num  in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] = 1
            
    single=[num for num,count in freq.items() if count  == 1]

    return single

nums=list(map(int,input().split()))
print(main(nums))
        
