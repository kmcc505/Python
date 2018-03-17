#Create a class 'Vehicle' which objects have three attributes (make, model, year)
#Then create method to print car year, make, model

class Vehicle:
    def __init__(self, make, model, yearnum):
        self.make = make
        self.model = model
        self.yearnum = yearnum

    def print_info(self):
        print(self.yearnum, self.make, self.model)

car = Vehicle('Toyota', 'Yaris', '2007')
car.print_info() 