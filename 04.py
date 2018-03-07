'''
This challenge is only meant to serve as practice (there is no correct answer).
Play around with polymorphism in Python. Here is an example animal class with an example animal (cat).

Try making more animal types than just cat!
'''

class Animal:
    # This is the constructor: e.g., Animal(name)
    def __init__(self, name):
        self.name = name

    # Abstract method. Subclasses must implement this or it will throw an error
    def speak(self):
        raise NotImplementedError('Subclass must implement abstract method')

class Cat(Animal): # This class inherits from Animal. This means it also inherits the constructor: Cat(name)
    def speak(self):
        return 'Nyan~'

# List of some animals
animals = [
    Cat('Mavis'), # This creates an instance of a cat
    Cat('Oreo'),
]

for animal in animals:
    print('My name is %s. %s' % (animal.name, animal.speak()))

