from .preprocessor import VideoPreprocessor
from ..flow import (
    FlowCaptured, 
    FlowPreprocessed, 
    FlowPreprocessedItem
)

class CV2VideoPreprocessor(VideoPreprocessor):
    def process(self, input: FlowCaptured) -> FlowPreprocessed:
        for item in input:
            yield FlowPreprocessedItem(
                original_frame=item.original_frame,
                processed_frame=item.original_frame
            )
