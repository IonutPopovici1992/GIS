# Some variables
x = 10
y = 20

# A function
def doSomething():
    print('Do something function')

# A class called point
class Point:

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def explain(self):
        print('My latitude = ' + str(self.latitude) + ' and my longitude = ' + str(self.longitude))
