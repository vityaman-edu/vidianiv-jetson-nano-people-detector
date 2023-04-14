from abc import ABC
from ..flow import (
    FlowCaptured, 
    FlowPreprocessed
)


class VideoPreprocessor(ABC):
    def process(self, input: FlowCaptured) -> FlowPreprocessed:
        raise NotImplementedError()
