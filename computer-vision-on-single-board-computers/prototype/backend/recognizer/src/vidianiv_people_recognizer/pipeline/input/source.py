from abc import ABC, abstractmethod
from .type import Video


class VideoSource(ABC):
    @abstractmethod
    def __enter__(self):
        raise NotImplementedError()

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError()
    
    @abstractmethod
    def __iter__(self) -> Video:
        raise NotImplementedError()
    
    @property
    def video(self) -> Video:
        return iter(self)
