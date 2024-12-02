# Problem statement
# You have been given an array/list ‘arr’ of length ‘N’, which contains single digit elements at every index. Your task is to return the sum of all elements of the array. But the final sum should also be a single digit.

# To keep the output single digit - you need to keep adding the digits of the output number till a single digit is left.

def magic_sum(array):
    
    total=sum(array)

    while total >=10:
        
        temp=str(total)
        result = 0

        for num in temp:
            
            result += int(num)
            
        total =result

    
    return total
            
a=[5, 8, 4, 9]
print(magic_sum(a))