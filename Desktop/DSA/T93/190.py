
def main(array):
    
    def quick_sort(arr):
        
        if len(arr)<=1:
            
            return arr
        
        else:
            
            mid=arr[len(arr)//2]
            left=[x for x in arr if x<mid]
            middle=[x for x in arr if x==mid]
            right=[ x for x in arr if x>mid]

            return quick_sort(left)+middle+quick_sort(right)

    
    temp=quick_sort(array)

    return temp
a=[1, 2, 3, 4, 5]
print(main(a))