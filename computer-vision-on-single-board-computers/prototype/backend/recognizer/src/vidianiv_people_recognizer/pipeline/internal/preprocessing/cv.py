from .preprocessor import (
    Video,
    FlowStream,
    VideoPreprocessor,
    PreprocessedFlowItem
)

class CV2VideoPreprocessor(VideoPreprocessor):
    def __call__(self, input: Video) -> FlowStream:
        for frame in input:
            yield PreprocessedFlowItem(
                id=frame.id,
                original_image=frame.image,
                processed_image=frame.image
            )
