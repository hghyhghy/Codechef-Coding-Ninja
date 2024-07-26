# The function accepts a character array ‘arr’ of size ‘n’ as its argument. Each element of ‘arr’ represents the status of a parking slot, where ‘S’ represents an empty slot and ‘X’ represents an occupied slot. The function needs to return the maximum number of cars that can be parked in the parking lot. It is assumed that two cars cannot occupy the same slot and cars can only park in consecutive empty slots.

def parking_cars(string):

    count=0
    max_car=0

    for char in string:

        if char == "S":

            count += 1

        else:

            max_car=max(max_car,count)
            count = 0


    cars= max(max_car,count)
    return cars

arr = "XXXSXXSXXSSXXSXX"
print(parking_cars(arr))