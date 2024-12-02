

def main(array):
    
    minimum=float("inf")
    maximum=float("-inf")

    for num in array:
        
        minimum=min(minimum,num)

        profit = num - minimum
        
        maximum=max(maximum,profit)

    
    return maximum

prices = [7, 1, 5, 3, 6, 4]
print(main(prices))