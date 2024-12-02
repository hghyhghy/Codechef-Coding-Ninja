# You have been given an array/list ‘arr’ of length ‘N’, which contains single digit elements at every index. Your task is to return the sum of all elements of the array. But the final sum should also be a single digit.

# To keep the output single digit - you need to keep adding the digits of the output number till a single digit is left.


def sum_of_digits(total):
    
    while total >=10:
        
        total = sum(int(digit) for digit in str(total))

    return total

def main(arr):
    
    total=sum(arr)

    return sum_of_digits(total)

arr = [5, 8, 4, 9]
print(main(arr))