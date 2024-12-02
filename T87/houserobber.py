# Problem statement
# Mr. X is a professional robber planning to rob houses along a street. Each house has a certain amount of money hidden.



# All houses along this street are arranged in a circle. That means the first house is the neighbour of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses are broken into on the same night.



# You are given an array/list of non-negative integers 'ARR' representing the amount of money of each house. Your task is to return the maximum amount of money Mr. X can rob tonight without alerting the police.

def house_robber(array:list[int])->int:
    
    n=len(array)
    
    if n == 0:
        
        return 0
    
    if n==1:
        
        return array[0]

    if n==2:
        
        return max(array[0],array[1])
    
    
    def max_looting(start,end):
        
        max_money =  0
        
        for i in range(start,end):
            
            current  = array[i]
            
            for j in range(i+2,end):
                
                current += array[j]
                
            max_money =  max(max_money,current)
            
        return max_money
    
    scenario = max_looting(0,n-1)
    scenario1= max_looting(1,n)
    
    return max(scenario,scenario1)

houses = [1 ,3 ,2 ,1]
print(house_robber(houses))