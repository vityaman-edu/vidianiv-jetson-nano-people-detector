from typing import NamedTuple
from jetson.inference import Detector
from jetson.video import ImageInput, ImageOutput
from service.reciever import Reciever


class RecognizerConfig(NamedTuple):
    detection_period: int


class Recognizer(NamedTuple):
    model: Detector
    video_input: ImageInput
    video_output: ImageOutput
    reciever: Reciever
    config: RecognizerConfig

    def run(self) -> None:
        i, period = 0, self.config.detection_period
        for image in self.video_input:
            if i == 0:
                objects = self.model.objects_on(image)
                self.reciever.take(objects)
            self.video_output.consume(image)
            i = (i + 1) % period
