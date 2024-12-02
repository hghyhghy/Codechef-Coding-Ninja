

#single element 

def main(array):
    
    freq={}

    for num in array:
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] = 1
            
    number=[num for num,count in freq.items() if count == 1]

    return number

a=[ 1, 1, 2, 3, 3, 4, 4]
print(main(a))