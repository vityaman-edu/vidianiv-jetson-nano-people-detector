from typing import NamedTuple, Collection
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

    def is_inside(self, other: 'Rectangle') -> bool:
        return other.left < self.left and \
            self.right < other.right and \
            other.top < self.top and \
            self.bottom < other.bottom
    
    def is_intersect(self, other: 'Rectangle') -> bool:
        if self.left > other.right or self.right < other.left:
            return False
        if self.top > other.bottom or self.bottom < other.top:
            return False
        return True
    
    def __and__(self, other: 'Rectangle') -> 'Rectangle':
        if not self.is_intersect(other):
            return Rectangle(left=0, right=0, top=0, bottom=0)
        left = max(self.left, other.left)
        right = min(self.right, other.right)
        top = max(self.top, other.top)
        bottom = min(self.bottom, other.bottom)
        return Rectangle(left, right, top, bottom)

    @property
    def area(self) -> float:
        return (self.right - self.left) * (self.bottom - self.top)


class Kind(NamedTuple):
    class_id: int
    label: str


class Detection(NamedTuple):
    confidence: float
    kind: Kind
    box: Rectangle
