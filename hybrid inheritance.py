#HYBRID INHERITANCE
class animals:
    def sound(self):
        print("animals make sounds")
class mammals(animals):
    def make_sound(self):
        print("mammals make sound")
class bird(animals):
    def makes_sound(self):
        print("birds make sound")
class bat(mammals,bird):
        pass
obj=bat()
obj.make_sound()
obj.sound()
obj.makes_sound()
