

#first missing positive 

def main(array):

    
    seen=set()

    for num  in array:
        
        if num > 0:
            
            seen.add(num)


    missing=1

    while missing in seen:
        
        missing +=1
        
    return missing

arr = [3, 4, -1, 1]
print(main(arr))