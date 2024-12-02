#subarray in a range 

def main(array:list[int],x:int,y:int)->int:
    
    count=0
    n=len(array)

    for i in range(n):
        
        maximum = array[i]

        for j in range(i,n):
            
            maximum=max(maximum,array[j])

            if x<=maximum<=y:
                
                count += 1
                
    return count

arr = [1, 2, 3, 4, 5]
X = 2
Y = 4
print(main(arr,X,Y))