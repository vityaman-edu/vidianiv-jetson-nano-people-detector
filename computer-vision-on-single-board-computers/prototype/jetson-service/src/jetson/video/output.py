from typing import NamedTuple
from .codec import Codec
from ..alias import VideoOutput, Image


class ImageOutputParameters(NamedTuple):
    codec: Codec
    bitrate: int


class ImageOutput:
    def __init__(self, address: str, parameters: ImageOutputParameters):
        self.out = VideoOutput(address, argv=[
            f'--headless',
            f'--bitrate={parameters.bitrate}',
            f'--output-codec={parameters.codec}'
        ])

    def consume(self, image: Image) -> None:
        self.out.Render(image)
