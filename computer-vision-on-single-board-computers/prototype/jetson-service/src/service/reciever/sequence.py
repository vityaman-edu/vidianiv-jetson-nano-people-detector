from typing import List, Collection
from .reciever import Reciever
from jetson.inference.detection import Detection


class SequenceReciever(Reciever):
    def __init__(self, reporters: List[Reciever]) -> None:
        self.recievers = reporters

    def take(self, detected_objects: Collection[Detection]) -> Collection[Detection]:
        for reciever in self.recievers:
            detected_objects = reciever.take(detected_objects)
        return detected_objects
