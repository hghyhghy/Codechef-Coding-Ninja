

#kth largest element 

def main(array,k):
    
    def quick(arr):
        
        if len(arr) <=1:
            
            return arr
        
        else:
            
            mid=arr[len(arr)//2]
            left=[x for x in arr if x>mid]
            middle=[x for x in arr if x==mid]
            right=[x for x in arr if x<mid]

            return quick(left)+middle+quick(right)

    
    temp=quick(array)
    return temp[:k]

n=int(input("enter"))
arr=list(map(int,input().split()))

print(main(arr,n))