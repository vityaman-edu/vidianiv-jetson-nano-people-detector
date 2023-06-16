from typing import Collection
from abc import ABC, abstractmethod
from jetson.inference.detection import Detection


class Reciever(ABC):
    @abstractmethod
    def take(self, detected_objects: Collection[Detection]) -> Collection[Detection]:
        raise NotImplementedError

