def buy_and_sell_stock(array:list[int])->int:
    
    n=len(array)
    maximum=0

    for i in range(n-1):
        
        if array[i+1] > array[i]:
            
            maximum += array[i+1]-array[i]

    
    return maximum

PRICES = [7, 1, 5, 4, 3, 6]
print(buy_and_sell_stock(PRICES))