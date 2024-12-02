# Find the largest number in an array

def find_largest(arr):
    
    def quick_sort(arr):
        
        if len(arr) <= 1:
            
            return arr
        
        else:
            
            mid = arr[len(arr)//2]

            left = [x for x in arr if x > mid]
            middle = [ x for x in arr if x  ==  mid]
            right =[x for x in arr if x  < mid]

            return quick_sort(left)+middle+quick_sort(right)

    temp=quick_sort(arr)

    return temp[0]

a=[10,5,9,11,3,2,6]
print(find_largest(a))
            