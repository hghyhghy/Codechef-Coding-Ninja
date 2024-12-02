def house_robber(array:list[int])->int:
    
    n=len(array)

    if n==0:
        
        return 0
    
    if n==1:
        
        return array[0]

    if n==2:
        
        return max(array[0],array[1])
    
    def max_looting(start,end):
        
        max_money=0
        
        for i in range(start,end):
            
            current = array[i]
            
            for j in range(i+2,end):
                
                current += array[j]

                max_money = max(max_money,current)

        
        return max_money
    
    scen1=max_looting(0,n-1)
    scen2=max_looting(1,n)
    
    return max(scen1,scen2)

houses = [1 ,3 ,2 ,1]
print(house_robber(houses))