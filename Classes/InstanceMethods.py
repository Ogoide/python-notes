class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance methods are methods shared by all objects of the same class
    def description(self):
        print(f'My name is {self.name} and I am {self.age} years old.')
    def speak(self, sound):
        print(f'{self.name} says {sound}.')

miles = Dog('Files', 12)
miles.description()  # My name is Files and I am 12 years old.
miles.speak('woof')  # My name is Files and I am 12 years old.
 