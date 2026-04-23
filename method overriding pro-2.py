class animal:
    def sound(self):
        print("this is base class of sounds")
class dog(animal):
    def sound(self):
        print("dogs sounds bow_bow")
class cat(animal):
    def sound(self):
        super().sound()
        print("cat sounde meow")
obj=cat()
obj.sound
        
