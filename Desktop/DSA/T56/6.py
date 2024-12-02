# Problem statement
# You are given the arrival and departure times of N trains at a railway station in a day. You need to find the minimum of platforms required for the railway station such that no train waits i.e No train should wait for the platform to be clear or free.

def platforms_needed(arr1,arr2):
    
    arr1.sort()
    arr2.sort()

    n=len(arr1)

    i=0
    j=0
    
    platform=0
    max_paltform=float("-inf")
    
    while i<n and j<n:
        
        if arr1[i] <= arr2[j]:
            
            platform += 1
            i += 1
            
        else:
            
            platform -= 1
            j += 1
            
        
        max_paltform=max(max_paltform,platform)
        
    return max_paltform

arrivals = [900, 940, 950, 1100, 1500, 1800]
departures = [910, 1200, 1120, 1130, 1900, 2000]

print(platforms_needed(arrivals,departures))