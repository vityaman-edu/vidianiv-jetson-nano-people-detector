from abc import ABC, abstractmethod
from ..flow import FlowCaptured


class VideoSource(ABC):
    @abstractmethod
    def __enter__(self):
        raise NotImplementedError()

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError()
    
    @abstractmethod
    def __iter__(self) -> FlowCaptured:
        raise NotImplementedError()
    
    @property
    def flow(self) -> FlowCaptured:
        return iter(self)
