from typing import NamedTuple
from ...core import Id, Image, Stream


class Frame(NamedTuple):
    id: Id
    image: Image

Video = Stream[Frame]
