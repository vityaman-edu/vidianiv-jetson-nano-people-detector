from typing import Collection, List, Set
from jetson.inference.detection import Detection
from .reciever import Reciever

class Deduplicator(Reciever):
    def __init__(self, overlap_threshold: float) -> None:
        self.area_threshold = overlap_threshold

    def take(self, detected_objects: Collection[Detection]) -> Collection[Detection]:
        return self.filtered(detected_objects)
    
    def duplicates(self, object: Detection, objects: Collection[Detection]) -> Collection[Detection]:
        dups: Set[Detection] = set()
        for other in objects:
            common = object.box & other.box
            biggest_area = min(object.box.area, other.box.area)
            if common.area / biggest_area > self.area_threshold:
                dups.add(other)
        return dups
        
    def filtered(self, objects: Collection[Detection]) -> Collection[Detection]:
        objects = set(objects)
        filtered: List[Detection] = []
        while len(objects) != 0:
            object = objects.pop()
            objects.difference_update(self.duplicates(object, objects))
            filtered.append(object)
        return filtered