# Inheritance is the process by which one class takes on the attributes and methods of another.
# Newly formed classes are called child classes, and the classes that you derive child classes
# from are called parent classes.

class Parent:
    # global class attribute
    hair_color = 'brown'
    eye_color = 'black'
    speaks = ['English']


# Creating a class that inherits another one - inherits all class attributes and methods, but can extend or override
class Child(Parent):
    # Overriding hair_color class attribute
    hair_color = 'blue'
    # Adding a new language to attribute speaks
    def __init__(self):
        super.__init__()
        self.speaks.append('German')


# hair_color inherited from Parent overridden by Child
print(Parent.hair_color)  # brown
print(Child.hair_color)  # blue

# eye_color inherited from Parent kept by Child
print(Parent.eye_color)  # black
print(Child.eye_color)  # black
