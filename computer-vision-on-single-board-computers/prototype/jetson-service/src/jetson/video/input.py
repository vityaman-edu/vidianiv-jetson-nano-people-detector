from ..alias import VideoSource, Image


class ImageInput:
    def __init__(self, address: str):
        self.source = VideoSource(address)

    def next_image(self) -> Image:
        return self.source.Capture()

    def __iter__(self) -> 'ImageInput':
        return self

    def __next__(self) -> Image:
        image = self.next_image()
        if image is None:
            raise StopIteration
        return image
