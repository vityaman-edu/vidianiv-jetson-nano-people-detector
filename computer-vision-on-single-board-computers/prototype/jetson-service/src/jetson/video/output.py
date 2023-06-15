from ..alias import VideoOutput, Image


class ImageOutput:
    def __init__(self, address: str):
        self.out = VideoOutput(address, argv=["--headless"])

    def consume(self, image: Image):
        return self.out.Render(image)
