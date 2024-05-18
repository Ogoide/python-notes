class One:
    # dunder method __init__ is used to assign attribute values to class instances
    def __init__(self, number):
        self.number = number

class Two:
    def __init__(self, number):
        self.number = number
    # dunder method __str__ is used to return a given value when a class instance is 'printed' as a string
    def __str__(self):
        return str(self.number)

um = One(1)
dois = Two(2)

print(um)  # <__main__.One object at 0x00000228F6C5E720>
print(dois)  # 2 - usage of __str__(self)