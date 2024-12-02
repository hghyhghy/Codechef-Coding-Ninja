

#finding duplicate

def main(array):
    
    freq={}

    for num in array:
        
        if num in freq:
            
            freq[num] +=1 
            
        else:
            
            freq[num]  = 1
            
    number=[num for num,count in freq.items() if count > 1]

    return number

arr = [1, 2, 3, 4, 5, 6, 7, 3]
print(main(arr))