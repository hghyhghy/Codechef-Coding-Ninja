

#sum of max and min


def main(array:list[int])->int:
    
    
    def bubble_sort(array):
        
        n=len(array)

        for  i in range(n):
            
            for j in range(0,n-i-1):
                
                if array[j]>array[j+1]:
                    
                    array[j],array[j+1]=array[j+1],array[j]

        
        return array
    
    new_array =  bubble_sort(array)

    return new_array[0] + new_array[len(new_array)-1]

n=list(map(int,input().split()))
print(main(n))