

#kth smallest element 

def main(array,k):
    
    def quick(array):
        
        if len(array) <=1:
            
            return array
        
        else:
            
            mid=array[len(array)//2]
            left=[x for x in array if x<mid]
            middle=[x for x in array if x==mid]
            right=[x for x in array if x>mid]

            return quick(left) + middle + quick(right)

    
    temp = quick(array)

    return temp[k-1]

arr=[4,1,3,6,7,2]
k=2

print(main(arr,k))