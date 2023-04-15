from abc import ABC, abstractmethod
from .type import Features

class Consumer(ABC):
    @abstractmethod
    def consume(self, input: Features):
        raise NotImplementedError()
