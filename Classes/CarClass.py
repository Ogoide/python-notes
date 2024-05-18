class Car():
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def description(self):
        print(f'The {self.color} car has {self.mileage} miles.')

car1 = Car('blue', 20000)
car2 = Car('red', 30000)

car1.description()
car2.description()