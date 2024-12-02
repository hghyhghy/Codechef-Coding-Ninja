
#sum of the elements of the array

def main(array):
    
    total = 0
    
    for num in array:
        
        total += num
        
    return total

num=list(map(int,input().split()))
print(main(num))