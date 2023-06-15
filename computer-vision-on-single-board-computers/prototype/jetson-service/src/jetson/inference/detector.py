from typing import Collection, NamedTuple, Optional
from ..alias import Image, DetectedObject, DetectNet


class Detector:
    class Parameters(NamedTuple):
        class Tracking(NamedTuple):
            min_frames: int
            drop_frames: int
            overlap_threshold: int
        name: str
        threshold: int
        tracking: Optional[Tracking] = None

    def __init__(self, parameters: Parameters):
        self.net = DetectNet(
            parameters.name, 
            threshold = parameters.threshold,
        )
        if parameters.tracking is not None:
            self.net.SetTrackingEnabled(True)
            self.net.SetTrackingParams(
                minFrames        = parameters.tracking.min_frames, 
                dropFrames       = parameters.tracking.drop_frames, 
                overlapThreshold = parameters.tracking.overlap_threshold,
            )

    def objects_on(self, image: Image) -> Collection[DetectedObject]:
        return self.net.Detect(image)
