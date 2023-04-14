import cv2 as cv
from .consumer import Consumer
from ..flow import FlowRecognized


class CVDisplay(Consumer):
    def __init__(self, name: str):
        self.name = name

    def consume(self, input: FlowRecognized):
        for item in input:
            if cv.waitKey(1) == ord('q'): break

            cv.imshow(self.name, item.marked_frame.image)
            print(item.features)
