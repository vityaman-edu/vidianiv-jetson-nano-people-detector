from typing import NamedTuple
from .codec import Codec
from ..alias import VideoSource, Image


class ImageInputParameters(NamedTuple):
    width: int
    height: int
    framerate: int
    codec: Codec
    flip: bool


class ImageInput:
    def __init__(self, address: str, parameters: ImageInputParameters):
        self.source = VideoSource(address, [
            f'--input-width={parameters.width}', 
            f'--input-height={parameters.height}',
            f'--input-rate={parameters.framerate}',
            # FIXME: nvbuffer_transform Failed
            # f'--input-flip={"rotate-180" if parameters.flip else "none"}',
            f'--input-codec={parameters.codec.value}',
        ])

    def next_image(self) -> Image:
        return self.source.Capture()

    def __iter__(self) -> 'ImageInput':
        return self

    def __next__(self) -> Image:
        image = self.next_image()
        if image is None:
            raise StopIteration
        return image
