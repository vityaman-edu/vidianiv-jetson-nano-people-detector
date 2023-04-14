from .recognizer import ObjectRecognizer
from ..flow import (
    FlowPreprocessed, 
    FlowRecognized,
    FlowRecognizedItem,
)
from ...core import (
    Feature,
    Object,
    Rectangle,
    Object,
    ObjectKind,
)


class YOLOV8Recognizer(ObjectRecognizer):
    def recognize(self, input: FlowPreprocessed) -> FlowRecognized:
        for item in input:
            yield FlowRecognizedItem(
                original_frame=item.original_frame,
                marked_frame=item.processed_frame,
                features={
                    Feature(
                        frame_id=item.original_frame.id,
                        object=Object(
                            kind=ObjectKind.PERSON,
                            shape=Rectangle(
                                center_x=0,
                                center_y=0,
                                width=0,
                                height=0
                            )
                        )
                    )
                }
            )
