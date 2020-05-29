"""simple oo example"""


class Pet:
    """ This class defines Pet, which is an animal kept by a human for domestic purposes" """
    def __init__(self, name):
        self.name = name
        self.hello = "I can't speak"

    def speak(self):
        """ sample - maybe lots of code in this """
        return self.hello

    def swim(self):
        return "splash"


class Dog(Pet):
    def __init__(self, name, license_num):
        Pet.__init__(self, name)  #single inheritance only. See 
                                  # w3 example
        self.hello = "woof"

        # i can specialize and add to subclass
        self.license_num = license_num

    def speak(self):
        """ reuse or embelish code from superclass """
        return Pet.speak(self)


mypet = Pet("Eric Fish")  # i am an object: an instance of the class Pet


print(mypet.name)
print(mypet.speak())
print(mypet.swim())

my_other_pet = Dog("Bogart", "AB56674")
print(my_other_pet.name)

# i just tell it to speak
print(my_other_pet.speak())

print(my_other_pet.license_num)
