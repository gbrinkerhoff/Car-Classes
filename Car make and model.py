# Name: Garrison Brinkerhoff
# Assignment: M02_Programming assignment
# Description: Car classes

class Vehicle():
    def __init___(self, year, make, model, doors, roof):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def getYear(self):
        return self.year

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getDoors(self):
        return self.doors

    def getRoof(self):
        return self.roof

    def setYear(self, year):
        self.year = year

    def setMake(self, make):
        self.make = make

    def setModel(self, model):
        self.model = model

    def setDoors(self, doors):
        self.doors = doors

    def setRoof(self, roof):
        self.roof = roof
        
class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        Vehicle.__init__(year, make, model, doors, roof)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def getYear(self):
        return self.year

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getDoors(self):
        return self.doors

    def getRoof(self):
        return self.roof

    def setYear(self, year):
        self.year

    def setMake(self, make):
        self.make

    def setModel(self, model):
        self.model

    def setDoors(self, doors):
        self.doors

    def setRoof(self, roof):
        self.roof

def main():
    myYear = input("Enter your cars year: ")
    myMake = input("Enter the make of your car: ")
    myModel = input("Enter the model of your car: ")
    myDoors = input("Enter how many doors are on your car: ")
    myRoof = input("Does your car have a sun roof (Y/N): ")

    myCar = Automobile(myYear, myMake, myModel, myDoors, myRoof)

    print()
    print("Year: " + myYear)
    print("Make: " + myMake)
    print("Model: " + myModel)
    print("Doors: " + myDoors)
    print("Sunroof: " + myRoof)


main()

   

