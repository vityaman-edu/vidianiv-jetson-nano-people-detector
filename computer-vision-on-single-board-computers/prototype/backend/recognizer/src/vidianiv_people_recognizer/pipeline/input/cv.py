from typing import Any
import cv2 as cv
from .source import VideoSource
from .type import Frame, Video

class CVVideoCapture(VideoSource):
    def __init__(self, source: Any):
        self.source = source
        self.capture = None

    def __enter__(self):
        self.capture = cv.VideoCapture(self.source)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.capture.release()

    def __iter__(self) -> Video:
        next_id = 0
        while self.capture.isOpened():
            is_correct, image = self.capture.read()
            
            if not is_correct:
                raise Exception('TODO: custom error')
            
            frame = Frame(next_id, image)
            next_id += 1
            
            yield frame
