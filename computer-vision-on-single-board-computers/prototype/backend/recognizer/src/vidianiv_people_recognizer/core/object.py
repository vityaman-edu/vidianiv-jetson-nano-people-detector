from typing import NamedTuple
from enum import Enum


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
