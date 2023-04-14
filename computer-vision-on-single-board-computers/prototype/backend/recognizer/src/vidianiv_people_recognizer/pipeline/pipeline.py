from typing import NamedTuple
from .capture import VideoSource
from .preprocessing import VideoPreprocessor
from .recognition import ObjectRecognizer
from .supply import Consumer


class Pipeline(NamedTuple):
    source: VideoSource
    preprocessor: VideoPreprocessor
    recognizer: ObjectRecognizer
    consumer: Consumer

    def start(self):
        with self.source as source:
            captured = source.flow
            preprocessed = self.preprocessor.process(captured)
            recognized = self.recognizer.recognize(preprocessed)
            self.consumer.consume(recognized)
