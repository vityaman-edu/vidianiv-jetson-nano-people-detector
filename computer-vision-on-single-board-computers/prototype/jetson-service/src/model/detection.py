from typing import NamedTuple
from jetson.alias import DetectedObject

'''
[<detectNet.Detection object>
   -- Confidence:  0.392337
   -- ClassID:     0
   -- TrackID:     0
   -- TrackStatus: 1
   -- TrackFrames: 4
   -- TrackLost:   2
   -- Left:    271.698
   -- Top:     0
   -- Right:   881.453
   -- Bottom:  705.348
   -- Width:   609.755
   -- Height:  705.348
   -- Area:    430090
   -- Center:  (576.576, 352.674)]
'''

class Rectangle(NamedTuple):
    left: float
    right: float
    top: float
    bottom: float


class Detection(NamedTuple):
    confidence: float
    box: Rectangle

    @classmethod
    def from_jetson(cls, other: DetectedObject) -> 'Detection':
        return Detection(
            confidence = other.Confidence,
            box = Rectangle(
                left = other.Left,
                right = other.Right,
                top = other.Top,
                bottom = other.Bottom,
            )
        )