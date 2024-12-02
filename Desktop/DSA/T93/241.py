

#majority element 

def main(array):
    
    freq={}

    for num in array:
        
        if num in freq:
            
            freq[num] +=1 
            
        else:
            
            freq[num] = 1
            
    result=[num for num,count in freq.items() if count > 1]

    return result

a=[3 ,2 ,2 ,1 ,5 ,2 ,3]
print(main(a))