

#remove duplicates 

def main(array):
    
    t=[]
    seen=set()

    for num in array:
        
        if num not in seen:
            
            seen.add(num)
            t.append(num)

    
    return len(t)

arr = [1, 1, 2, 3, 3, 4, 5]
print(main(arr))