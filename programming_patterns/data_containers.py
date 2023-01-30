from enum import Enum
from datetime import date
from typing import TypedDict
from dataclasses import dataclass


class PersonIDType(str, Enum):
    SSN = 'SSN'
    PASSPORT = 'PASSPORT'


class Person:
    """
    Main benefit over TypeDict is required fields. TypedDict will allow any key/value pair to be added.
    There are no other real benefits of Person over TypeDict or DataClass, when using the class as
    a data container.

    Examples:
    >>> person = Person()
    Traceback (most recent call last):
    ...
    TypeError: __init__() missing 4 required positional arguments: 'name', 'dob', 'identifier', and 'identifier_type'
    >>> person = Person('John Doe', '1970-01-01', '123456789', PersonIDType.SSN)
    >>> person.random = ''
    >>> person.random
    ''
    """
    def __init__(self, name: str, dob: date, identifier: str, identifier_type: PersonIDType):
        self.name = name
        self.dob = dob
        self.identifier = identifier
        self.identifier_type = identifier_type



class PersonTypedDict(TypedDict):
    """
    TypedDict does not validate object creation, allows for arbitrary data to be added. However,
    it is a dictionary so json dumps works out of the box.

    Examples:
    >>> person = PersonTypedDict()
    >>> person
    {}
    >>> person = PersonTypedDict(name='John Doe', dob='1970-01-01', identifier='123456789', identifier_type=PersonIDType.SSN)
    >>> person
    {'name': 'John Doe', 'dob': '1970-01-01', 'identifier': '123456789', 'identifier_type': <PersonIDType.SSN: 'SSN'>}
    >>> person['random'] = ''
    >>> person
    {'name': 'John Doe', 'dob': '1970-01-01', 'identifier': '123456789', 'identifier_type': <PersonIDType.SSN: 'SSN'>, 'random': ''}
    >>> from json import dumps
    >>> dumps(person)
    '{"name": "John Doe", "dob": "1970-01-01", "identifier": "123456789", "identifier_type": "SSN", "random": ""}'
    """
    name: str
    dob: str
    identifier: str
    identifier_type: PersonIDType


@dataclass(frozen=True)
class PersonDataClassFrozen:
    """
    Dataclasses validate that input is given for all fields. Allows for json dumps after usage of asdict.
    Can use Frozen to ensure object cannot be modified after creation.

    Examples:
    >>> person = PersonDataClassFrozen()
    Traceback (most recent call last):
    ...
    TypeError: __init__() missing 4 required positional arguments: 'name', 'dob', 'identifier', and 'identifier_type'
    >>> person = PersonDataClassFrozen(name='John Doe', dob='1970-01-01', identifier='123456789', identifier_type=PersonIDType.SSN)
    >>> person
    PersonDataClassFrozen(name='John Doe', dob='1970-01-01', identifier='123456789', identifier_type=<PersonIDType.SSN: 'SSN'>)
    >>> person.random = ''
    Traceback (most recent call last):
    ...
    dataclasses.FrozenInstanceError: cannot assign to field 'random'
    >>> person.name = 'Jane Doe'
    Traceback (most recent call last):
    ...
    dataclasses.FrozenInstanceError: cannot assign to field 'name'
    >>> from dataclasses import asdict
    >>> asdict(person)
    {'name': 'John Doe', 'dob': '1970-01-01', 'identifier': '123456789', 'identifier_type': <PersonIDType.SSN: 'SSN'>}
    >>> from json import dumps
    >>> dumps(asdict(person))
    '{"name": "John Doe", "dob": "1970-01-01", "identifier": "123456789", "identifier_type": "SSN"}'
    """
    name: str
    dob: date
    identifier: str
    identifier_type: PersonIDType


@dataclass()
class PersonDataClass:
    """
    Dataclasses validate that input is given for all fields. Allows for json dumps after usage of asdict.
    Without frozen attributes can be added and modified. However, they will not be included in json dumps for
    randomly added attributes.

    Examples:
    >>> person = PersonDataClass()
    Traceback (most recent call last):
    ...
    TypeError: __init__() missing 4 required positional arguments: 'name', 'dob', 'identifier', and 'identifier_type'
    >>> person = PersonDataClass(name='John Doe', dob='1970-01-01', identifier='123456789', identifier_type=PersonIDType.SSN)
    >>> person
    PersonDataClass(name='John Doe', dob='1970-01-01', identifier='123456789', identifier_type=<PersonIDType.SSN: 'SSN'>)
    >>> person.random = ''
    >>> person.name = 'Carl'
    >>> from dataclasses import asdict
    >>> asdict(person)
    {'name': 'Carl', 'dob': '1970-01-01', 'identifier': '123456789', 'identifier_type': <PersonIDType.SSN: 'SSN'>}
    >>> from json import dumps
    >>> dumps(asdict(person))
    '{"name": "Carl", "dob": "1970-01-01", "identifier": "123456789", "identifier_type": "SSN"}'
    """
    name: str
    dob: date
    identifier: str
    identifier_type: PersonIDType


if __name__ == "__main__":
    import doctest

    doctest.testmod()