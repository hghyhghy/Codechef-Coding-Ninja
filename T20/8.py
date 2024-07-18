


# The function takes an integral arr which is of the size or length of its arguments. Return the sum of the second smallest element at odd position ‘arr’ and the second largest element at the even position.    

def largesmallsum(arr):

    if not arr or len(arr) <=3 :

        return 0 
    
    
    odd_positions=[arr[i] for i in range(len(arr)) if i % 2 != 0]
    even_positions=[arr[i] for i in range(len(arr)) if i % 2 == 0]

    odd_positions.sort()
    element1 = odd_positions[1]

    even_positions.sort(reverse=True)
    element2= even_positions[1]

    return element1+element2


arr=[3 ,2 ,1 ,7 ,5 ,4]

print(largesmallsum(arr))