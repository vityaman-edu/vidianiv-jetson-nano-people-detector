from abc import ABC
from typing import NamedTuple
from ..flow import Id, Video, Image, FlowStream

class PreprocessedFlowItem(NamedTuple):
    id: Id
    original_image: Image
    processed_image: Image

class VideoPreprocessor(ABC):
    def __call__(self, input: Video) -> FlowStream:
        raise NotImplementedError()
