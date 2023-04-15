from .recognizer import (
    ObjectRecognizer,
    Stream,
    PreprocessedFlowItem,
    Features,
)
from ...output import (
    Feature, 
    Object, 
    ObjectKind, 
    Rectangle
)

class YOLOV8Recognizer(ObjectRecognizer):
    def __call__(self, input: Stream[PreprocessedFlowItem]) -> Features:
        for item in input:
            yield Feature(
                id=item.id,
                original_image=item.original_image,
                objects={
                    Object(
                        kind=ObjectKind.PERSON,
                        shape=Rectangle(
                            center_x=0,
                            center_y=0,
                            width=0,
                            height=0
                        )
                    )
                },
            )
