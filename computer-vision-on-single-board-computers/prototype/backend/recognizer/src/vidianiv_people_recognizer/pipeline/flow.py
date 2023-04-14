from typing import NamedTuple, Set
from ..core import Feature, Frame, Stream


# Stage 1: Camera -> Preprocessor
class FlowCapturedItem(NamedTuple):
    original_frame: Frame

FlowCaptured = Stream[FlowCapturedItem]


# Stage 2: Preprocessor -> Recognizer
class FlowPreprocessedItem(NamedTuple):
    original_frame: Frame
    processed_frame: Frame

FlowPreprocessed = Stream[FlowPreprocessedItem]


# Stage 3: Recognizer -> Client
class FlowRecognizedItem(NamedTuple):
    original_frame: Frame
    marked_frame: Frame
    features: Set[Feature]

FlowRecognized = Stream[FlowRecognizedItem]
