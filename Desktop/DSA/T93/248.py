

#single element from the array 

def main(array):
    
    freq={}

    for num  in array:
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] = 1
            
    number=[num for num,count in freq.items() if count == 1]

    return number

a= [1,1,2,2,4,5,5]
print(main(a))