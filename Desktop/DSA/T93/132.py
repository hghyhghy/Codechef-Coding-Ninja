

#minimum no of platforms needed 

def main(arr1,arr2):

    n=len(arr1)

    i=j=0
    platform=0
    max_platform=float("-inf")
    
    arr1.sort()
    arr2.sort()
    
    while i<n and j<n:
        
        if arr1[i] <= arr2[j]:
            
            platform += 1
            i +=1
            
        
        else:
            
            platform -=1
            j += 1
            

        max_platform = max(max_platform,platform)
        
    return max_platform

arrivals = [900, 940, 950, 1100, 1500, 1800]
departures = [910, 1200, 1120, 1130, 1900, 2000]

print(main(arrivals,departures))
    
