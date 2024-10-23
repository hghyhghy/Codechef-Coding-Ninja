# You are given the list of costs of pants in an array “pants”, shirts in an array “shirts”, shoes in an array “shoes”, and skirts in an array “skirts”. You are also given a budget amount ‘X’ to spend. You want to buy exactly 1 item from each list. Your task is to determine the total number of possible combinations that you can buy, given that the total amount of your purchase does not exceed your budget amount.

def possible_combinations(pants,shirts,shoes,skirts,price):
    
    valid_combination= 0
    
    for pant in pants:
        
        for shirt in shirts:
            
            for shoe in shoes:
                
                for skirt in skirts:
                    
                    total_price=  pant+shirt+shoe+skirt
                    
                    if total_price <= price:
                        
                        valid_combination += 1
                        
                        
                        
    return valid_combination

pants = [10, 20, 30]
shirts = [5, 10]
shoes = [10, 20, 30]
skirts = [5, 15]
X = 50

print(possible_combinations(pants,shirts,shoes,skirts,X))