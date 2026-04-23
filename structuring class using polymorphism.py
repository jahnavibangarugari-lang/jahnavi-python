class vehicles:
    def move(self):
        print("vehicle moves")
class car(vehicles):
    def move(self):
        print("car used to drive")
class boat(vehicles):
    def move(self):
        print("boat sails in river")
v1=car()
v1.move()
v2=boat()
v2.move()
