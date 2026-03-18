🧐 What is Polymorphism?

Polymorphism is a core concept in Object-Oriented Programming (OOP). It allows different classes to be treated as instances of the same class through the same interface. In this code, Dog, Cat, and Parrot all implement a make_sound() method, allowing us to iterate through them and call the same function name regardless of the animal type.

💻 Code Snippet

Python
class Dog:
    def make_sound(self):
        return "Woof!"

class Cat:
    def make_sound(self):
        return "Meow!"

class Parrot:
    def make_sound(self):
        return "Squawk!"

# Polymorphism in action
for pet in [Dog(), Cat(), Parrot()]:
    print(pet.make_sound())
🚀 How it Works
Shared Interface: Each class has a method named make_sound().

Generic Execution: We create a list containing instances of different classes.

Dynamic Dispatch: The for loop doesn't need to know if the pet is a Dog or a Cat; it simply calls .make_sound() and Python handles the rest.

🛠️ Requirements
Python 3.x

📝 Output
Plaintext
Woof!
Meow!
Squawk!
