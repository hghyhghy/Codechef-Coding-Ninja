 
 
 #recursive quick sort 
 
def main(array):
    
    if len(array) <=1:
        
        return array
    
    else:
        
        mid=array[len(array)//2]

        left=[x for x in array if x<mid]
        middle=[x for x in array if x == mid]
        right=[x for x in array if x >mid]


        return main(left)+middle+main(right)

array = [ 4, 2, 1, 5, 3 ]
print(main(array))