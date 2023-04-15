from typing import NamedTuple, Set
from enum import Enum
from ...core import Id, Stream, Image

class Rectangle(NamedTuple):
    center_x: int
    center_y: int
    width: int
    height: int

class ObjectKind(Enum):
    PERSON = 'Person'

class Object(NamedTuple):
    kind: ObjectKind
    shape: Rectangle

class Feature(NamedTuple):
    id: Id
    original_image: Image
    objects: Set[Object]

Features = Stream[Feature]
