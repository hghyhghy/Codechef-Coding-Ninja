# alice has a magical shoe of 1 par by which he can climb 3 stairs at once , he wants to reach the roof of three house the stairs 
# to the roof of each house is represnted as an array but alice can reach only those are multiple of 3 help him to find 


def possible_roofs_to_reach(arr):
    
    count=0
    
    for i in range(len(arr)):
        
        if arr[i] % 3  == 0:
            
            count += 1
            
    return count

a=[12,21,3,4]
print(possible_roofs_to_reach(a))