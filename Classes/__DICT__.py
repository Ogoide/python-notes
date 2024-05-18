import pprint

class SampleClass:
    class_attr = 100

    def __init__(self, instance_attr):
        self.instance_attr = instance_attr

    def method(self):
        print(f"Class attribute: {self.class_attr}")
        print(f"Instance attribute: {self.instance_attr}")

# .__dict__ will display a dict data type corresponding to the classes attributes and methods
pprint.pprint(SampleClass.__dict__)
# mappingproxy({'__dict__': <attribute '__dict__' of 'SampleClass' objects>,
#               '__doc__': None,
#               '__init__': <function SampleClass.__init__ at 0x0000017A578331A0>,
#               '__module__': '__main__',
#               '__weakref__': <attribute '__weakref__' of 'SampleClass' objects>,
#               'class_attr': 100,
#               'method': <function SampleClass.method at 0x0000017A57A94EA0>})
print(SampleClass.__dict__['class_attr'])  # 100