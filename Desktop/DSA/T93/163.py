

#container with max water 


def main(array):
    
    n=len(array)
    max_water=0
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            height =  min(array[i],array[j])

            width = j-i
            
            area =  width * height
            
            max_water =  max(max_water,area)

    return max_water

arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(main(arr))