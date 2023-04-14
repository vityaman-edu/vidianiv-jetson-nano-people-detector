from abc import ABC
from ..flow import (
    FlowPreprocessed, 
    FlowRecognized
)


class ObjectRecognizer(ABC):
    def recognize(self, input: FlowPreprocessed) -> FlowRecognized:
        raise NotImplementedError()
