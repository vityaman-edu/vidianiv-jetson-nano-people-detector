from typing import Iterable
from ultralytics import YOLO
from .recognizer import (
    ObjectRecognizer,
    Stream,
    PreprocessedFlowItem,
    Features,
)
from ....core import Image
from ...output import (
    Feature, 
    Object, 
    ObjectKind, 
    Rectangle
)
import cv2 as cv


class YOLOV8Recognizer(ObjectRecognizer):
    def __init__(self, path: str = 'yolov8n.pt'):
        self.model = YOLO(path)

    def __call__(self, input: Stream[PreprocessedFlowItem]) -> Features:

        objects, i = {}, 0
        for item in input:
            
            i = (i + 1) % 5
            if i == 0:
                objects = set(self.detect(item.processed_image))
            
            self.draw_objects(item.original_image, objects)
            
            yield Feature(
                id=item.id,
                original_image=item.original_image,
                objects=objects,
            )
    
    def detect(self, image: Image):
        for result in self.model.predict(image, classes=[0], max_det=50):
            for box in result.boxes:
                x, y, w, h = map(int, box.xywh[0])
                yield Object(
                    kind=ObjectKind.PERSON,
                    shape=Rectangle(
                        center_x=x,
                        center_y=y,
                        width=w,
                        height=h
                    )
                )   

    def draw_objects(self, image: Image, objects: Iterable[Object]):
        color = (255, 255, 0)
        count = 0

        for obj in objects:
            x, y, w, h = obj.shape
            count += 1

            cv.rectangle(image, (x - w // 2, y - h // 2), (x + w // 2, y + h // 2), color, 1)
            cv.putText(image, f'{obj.kind.value}', (x - w // 2, y - h // 2), cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

        cv.putText(image, f'Count: {count}', (40, 70), cv.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 2)
