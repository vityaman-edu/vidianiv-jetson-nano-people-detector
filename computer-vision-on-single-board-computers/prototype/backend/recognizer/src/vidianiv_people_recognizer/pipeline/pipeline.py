from typing import NamedTuple
from .input import VideoSource
from .internal import Flow
from .output import Consumer

class Pipeline(NamedTuple):
    source: VideoSource
    flow: Flow
    consumer: Consumer

    def start(self):
        with self.source as source:
            input = source.video
            output = self.flow.process(input)
            self.consumer.consume(output)
