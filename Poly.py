class Dog:
    def make_sound(self):
        return "Woof!"

class Cat:
    def make_sound(self):
        return "Meow!"

class Parrot:
    def make_sound(self):
        return "Squawk!"


for pet in [Dog(), Cat(), Parrot()]:
    print(pet.make_sound())
