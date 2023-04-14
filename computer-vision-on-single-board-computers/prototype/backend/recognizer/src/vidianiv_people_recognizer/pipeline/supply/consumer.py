from abc import ABC, abstractmethod
from ..flow import FlowRecognized


class Consumer(ABC):
    @abstractmethod
    def consume(self, input: FlowRecognized):
        raise NotImplementedError()
