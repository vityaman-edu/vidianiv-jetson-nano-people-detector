from typing import Collection, List, Set
from abc import ABC, abstractmethod
from jetson.inference.detection import Detection, Rectangle


class Reporter(ABC):
    @abstractmethod
    def report(self, detected_objects: Collection[Detection]) -> None:
        raise NotImplementedError


class ConsoleReporter(Reporter):
    def __init__(self, tag: str, sep: str, verbose: bool, area_threshold: float) -> None:
        self.tag = tag
        self.sep = sep
        self.verbose = verbose
        self.area_threshold = area_threshold

    def report(self, detected_objects: Collection[Detection]) -> None:
        self.print(self.filtered(detected_objects))

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
    
    def print(self, objects: Collection[Detection]) -> None:
        if len(objects) == 0: return
        tag, sep = self.tag, self.sep
        print(f'[{tag}] {sep * 3} Detected {len(objects)} objects {sep * 3}')
        for o in objects:
            print(f'[{tag}] Detection \'{o.kind.label}\' {o.confidence:.2f}')
            if self.verbose:
                print(f'[{tag}]   left: {o.box.left:.2f}, right:  {o.box.right:.2f}')
                print(f'[{tag}]   top:  {o.box.top:.2f} , bottom: {o.box.bottom:.2f}')
        print(f'[{tag}] {sep * 3} {sep * 14} {sep * 3}')
        print(f'[{tag}]')
