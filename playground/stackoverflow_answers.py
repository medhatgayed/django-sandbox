__author__ = 'medhat'

data = [['Name', 'Age', 'Gender', 'Height', 'HairColor'],
 ['Jay', '12', 'M', '123cm', 'Black'],
 ['Marie', '13', 'F', '100cm', 'Red'],
 ['Dan', '16', 'M', '200cm', 'Brown']
]

from collections import namedtuple
Person = namedtuple('Person', data[0])
persons = {}
del data[0]
for p in data:
    person = Person._make(p)
    persons['{};{};{}'.format(person.Name, person.Age, person.Gender)] = dict(person._asdict())
print(persons)


