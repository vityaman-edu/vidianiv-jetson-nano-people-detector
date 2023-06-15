from typing import NamedTuple, Callable
from jetson.inference import Detector
from jetson.video import ImageInput, ImageOutput
from model import Detection


class Recognizer(NamedTuple):
    class Config(NamedTuple):
        detection_period: int

    model: Detector
    video_input: ImageInput
    video_output: ImageOutput
    objects_output: Callable[[Detection], None]
    config: Config

    def run(self):
        i, period = 0, self.config.detection_period
        for image in self.video_input:
            if i == 0:
                objects = self.model.objects_on(image)
                objects = list(map(Detection.from_jetson, objects))
                self.objects_output((objects))
            self.video_output.consume(image)
            i = (i + 1) % period
