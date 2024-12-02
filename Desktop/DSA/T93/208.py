

#smallest in two array

def main(arr1,arr2):
    
    r=[]


    for a in arr1:
        
        count = 0
        
        for b in arr2:
            
            if b>=a:
                
                count += 1
                
                r.append(b)

    return r

A = [3, 5, 7]
B = [1, 2, 3, 4, 5, 6]

print(main(A,B))