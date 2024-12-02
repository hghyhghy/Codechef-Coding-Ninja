# Design a class Car having parameterized constructor that takes two arguments as an input i.e noOfGear and color and a printCarInfo method that prints the CarInfo i.e noOfGear and color.

# Design another class RaceCar having parameterized constructor has an additional attribute maxSpeed and printRaceCarInfo method that prints the RaceCarInfo i.e noOfGear, color and maxSpeed.

# Note: You have to create an object of class RaceCar and call the printRaceCarInfo method.

class Car:
    
    def __init__(self,gear,color):
        
        self.gear=gear
        self.color=color
        
    def info(self):
        
        print(f"No of gear{self.gear} , car color {self.color}")


class Racingcar(Car):
    
    def __init__(self,gear,color,speed):
        
        super().__init__(gear,color)
            
        self.speed=speed
    
    def inforacing_car(self):
        
        print(f"No of gear {self.gear} , car color {self.color} , with max speed of {self.speed}")


race_car = Racingcar(6, "Red", 220)
race_car.inforacing_car()
        