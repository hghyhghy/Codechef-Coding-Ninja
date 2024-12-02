

#minimum in rotated sorted array

def  main(array:list[int])->int:
    
    n=len(array)
    minimum= array[0]

    for i in range(n):
        
        if array[i]<minimum:
            
            minimum =  array[i]

    return minimum

nums=list(map(int,input().split()))
print(main(nums))