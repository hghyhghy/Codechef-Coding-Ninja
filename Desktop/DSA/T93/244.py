

#no of occurances 

def main(array,target):
    
    freq={}

    for num in array:
        
        if num in freq:
            
            freq[num] +=1 
            
        else:
            
            freq[num] = 1
            
    return freq.get(target,0)


arr = [1, 1, 1, 2, 2, 3, 3]
x = 3

print(main(arr,x))