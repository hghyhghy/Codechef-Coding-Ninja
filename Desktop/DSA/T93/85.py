
#search in the rotated sorted array 

def main(array,target):
    
    n=len(array)

    for i in range(n):
        
        if array[i]== target:
            
            return i
        
    return -1

target=int(input("enter"))
arr=list(map(int,input().split()))
print(main(arr,target)) 