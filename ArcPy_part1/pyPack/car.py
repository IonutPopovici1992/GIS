class Car:

    def __init__(self, color, numberOfDoors, tireSize):
        self.color = color
        self.numberOfDoors = numberOfDoors
        self.tireSize = tireSize

    def drive(self):
        print('I am driving')

    def turnRight(self):
        print('Turning right')

    def reverse(self):
        print('Reverse')
# End of class definition
#------------------------------------------------------
#------------------------------------------------------
# Using the class to create objects and use the objects

car1 = Car('green', 4, 15)
car2 = Car('pink', 2, 13)
car3 = Car('gray', 4, 13)

car1.tireSize = 16
car2.color = 'Yellow'
car3.drive()
car2.reverse()
