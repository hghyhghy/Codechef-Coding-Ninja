# You are given an array/list 'prices' where the elements of the array represent the prices of the stock as they were yesterday and indices of the array represent minutes. Your task is to find and return the maximum profit you can make by buying and selling the stock. You can buy and sell the stock only once.

def best_time_buy_sell_stock(array):
    
    min_value= array[0]

    for index in range(len(array)):
        
        if array[index] < min_value:
            
            min_value = array[index]
        
        max_value=0
        
        for i in range(min_value,len(array)):
            
            if array[i] > max_value:
                
                max_value = array[i]

                    
    return max_value-min_value

prices = [7, 1, 5, 3, 6, 4]
print((best_time_buy_sell_stock(prices)))