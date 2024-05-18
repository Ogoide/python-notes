# Classes can be changed dynamically, adding or removing attributes as needed
from pprint import pprint

class Record:
    pass


john = {
    "name": "John Doe",
    "position": "Python Developer",
    "department": "Engineering",
    "salary": 80000,
    "hire_date": "2020-01-01",
    "is_manager": False,
}

john_records = Record()

for k, v in john.items():
    # setattr(instance, key, value) adds a new attribute to the instance of a class as key = value
    setattr(john_records, k, v)

pprint(john_records.__dict__)
# {'department': 'Engineering',
#  'hire_date': '2020-01-01',
#  'is_manager': False,
#  'name': 'John Doe',
#  'position': 'Python Developer',
#  'salary': 80000}
