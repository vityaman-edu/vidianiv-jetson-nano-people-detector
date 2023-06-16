from typing import Collection, List, Set
from datetime import datetime
from jetson.inference.detection import Detection
from .reciever import Reciever


class ConsoleReciever(Reciever):
    def __init__(self, tag: str, sep: str, verbose: bool) -> None:
        self.tag = tag
        self.sep = sep
        self.verbose = verbose

    def take(self, detected_objects: Collection[Detection]) -> Collection[Detection]:
        return self.print(detected_objects)
    
    def print(self, objects: Collection[Detection]) -> Collection[Detection]:
        if len(objects) == 0: return objects
        time = datetime.now().strftime("%H:%M:%S")
        tag, sep = self.tag, self.sep
        print(f'[{tag}] {sep * 3} Detected {len(objects)} objects at {time} {sep * 3}') 
        for o in objects:
            print(f'[{tag}] Detection \'{o.kind.label}\' {o.confidence:.2f}')
            if self.verbose:
                print(f'[{tag}]   left: {o.box.left:.2f}, right:  {o.box.right:.2f}')
                print(f'[{tag}]   top:  {o.box.top:.2f} , bottom: {o.box.bottom:.2f}')
        print(f'[{tag}] {sep * 3} {sep * 14} {sep * 3}')
        print(f'[{tag}]')
        return objects
