from typing import Iterable, NamedTuple
from .object import Object
import cv2 as cv


FrameId = int

Image = cv.Mat

class Frame(NamedTuple):
    id: FrameId
    image: Image

Stream = Iterable

class Feature(NamedTuple):
    frame_id: FrameId
    object: Object
