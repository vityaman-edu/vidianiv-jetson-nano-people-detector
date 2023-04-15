import cv2 as cv
from .consumer import Consumer, Features


class CVDisplay(Consumer):
    def __init__(self, name: str):
        self.name = name

    def consume(self, input: Features):
        for item in input:
            if cv.waitKey(1) == ord('q'): break
            cv.imshow(self.name, item.original_image)
            print(item.id, item.objects)
