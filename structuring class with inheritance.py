class vehicles:
    def move(self):
        print("vehicles are moves")
class car(vehicles):
    def drive(self):
        print("drive from one place to another")
class bike(vehicles):
    def ride(self):
        print("bike rides")
c=car()
c.drive()
c.move()
b=bike()
b.ride()
b.move()
