from abc import ABC, abstractmethod
from ..preprocessing import PreprocessedFlowItem
from ..flow import Stream, Features

class ObjectRecognizer(ABC):
    @abstractmethod
    def __call__(self, input: Stream[PreprocessedFlowItem]) -> Features:
        raise NotImplementedError()
