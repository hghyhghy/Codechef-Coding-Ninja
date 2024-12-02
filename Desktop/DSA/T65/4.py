# Problem statement
# Design a class called Rectangle. It contains two data members as length(L) and breadth(B); and a member function getArea(). The member function computes the area of the given rectangle and returns it to the caller.

# Note:

# Area of a rectangle = length x breadth
# Data Members:
# 1. length: Length of the rectangle
# 2. breadth: Breadth of the rectangle 
# Member Functions:
# 1. getArea(): that calculates the area of the rectangle and returns the value.
# Note:

# You do not have to take input, just create the Class and set the name of the Data Members and function as given in the above discription.

class Rectangle:
    
    def __init__(self,length=0,breadth=0):
        
        self.length=length
        self.breadth=breadth
        
    def getArea(self):
        
        return self.length * self.breadth
    
    
rect = Rectangle(5, 3)
print("Area of the rectangle:", rect.getArea())