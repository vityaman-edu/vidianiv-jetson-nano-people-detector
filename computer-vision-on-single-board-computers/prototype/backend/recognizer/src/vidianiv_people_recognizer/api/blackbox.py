from ..pipeline import (
    Pipeline,
    VideoSource,
    Consumer,
    Flow, 
    CV2VideoPreprocessor,
    YOLOV8Recognizer
)

def blackbox(source: VideoSource, consumer: Consumer) -> Pipeline:
    return Pipeline(
        source=source,
        flow=Flow(
            enter=CV2VideoPreprocessor(),
            internal=[],
            exit=YOLOV8Recognizer()
        ),
        consumer=consumer
    )
