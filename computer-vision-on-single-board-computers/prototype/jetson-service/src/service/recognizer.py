from jetson.inference import Detector
from jetson.video import ImageInput, ImageOutput


class Recognizer:
    def __init__(self, model: Detector, input: ImageInput, output: ImageOutput):
        self.model  = model
        self.input  = input
        self.output = output

    def run(self):
        for image in self.input:
            _ = self.model.objects_on(image)
            self.output.consume(image)
