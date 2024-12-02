# The function accepts two positive integers ‘r’ and ‘unit’ and a positive integer array ‘arr’ of size ‘n’ as its argument ‘r’ represents the number of rats present in an area, ‘unit’ is the amount of food each rat consumes and each ith element of array ‘arr’ represents the amount of food present in ‘i+1’ house number, where 0 <

def amount_of_food(arr,r,unit,n):

   
    
    required_food=r*unit

    available_food=0
    count = 0

    for i in range(n):

        available_food += arr[i]

        count += 1

        if available_food >= required_food:

            return count
        
    return 0

n=8
r = 7  # Number of rats
unit = 2  # Food units each rat consumes
arr = [2, 8, 3, 5, 7, 4, 1, 2]  

print(amount_of_food(arr,r,unit,n))

        

