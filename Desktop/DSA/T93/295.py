


#most frequent element

def main(array):
    
    freq={}

    for num in array:
        
        if num in freq:
            
            freq[num] +=1
            
        else:
            
            freq[num] = 1
            
    number=[num for num,count in freq.items() if count > 1]

    return number

array = [1, 2, 3, 2, 4, 5, 1, 6, 7, 5]
print(main(array))