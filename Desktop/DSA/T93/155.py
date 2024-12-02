
#calculate minimum and maximum

def main(array:list[int])->int:
    
    minimum = array[0]
    maximum = array[0]

    for num in array:
        
        if num > maximum:
            
            maximum =  num
            
        if num  < minimum:
            
            minimum = num
            
    return maximum,minimum

nums=list(map(int,input().split()))
print(main(nums))