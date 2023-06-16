from typing import Collection, NamedTuple, Optional
from enum import Enum
from .detection import Detection, Rectangle, Kind
from ..alias import Image, DetectNet, DetectedObject


class ModelName(Enum):
    PEOPLENET = 'peoplenet'
    PEOPLENET_PRUNED = 'peoplenet-pruned'
    PEDNET = 'pednet'


class TrackingParameters(NamedTuple):
    min_frames: int
    drop_frames: int
    overlap_threshold: float


class Overlay(Enum):
    BOX = 'box'
    LABEL = 'labels'
    CONF = 'conf'
    NONE = 'none'


class DetectorParameters(NamedTuple):
    name: ModelName
    threshold: float
    tracking: Optional[TrackingParameters] = None
    overlay: Collection[Overlay] = { Overlay.NONE }


class Detector:
    def __init__(self, parameters: DetectorParameters):
        csv_overlay = ",".join(list(map(lambda o: o.value, parameters.overlay)))
        self.net = DetectNet(
            parameters.name.value, [
                f'--network={parameters.name.value}',
                f'--overlay={csv_overlay}',
            ],
            threshold = parameters.threshold,
        )
        if parameters.tracking is not None:
            self.net.SetTrackingEnabled(True)
            self.net.SetTrackingParams(
                minFrames        = parameters.tracking.min_frames, 
                dropFrames       = parameters.tracking.drop_frames, 
                overlapThreshold = parameters.tracking.overlap_threshold,
            )

    def objects_on(self, image: Image) -> Collection[Detection]:
        def convert(o: DetectedObject) -> Detection:
            return Detection(
                confidence = o.Confidence,
                kind = Kind(o.ClassID, self.net.GetClassLabel(o.ClassID)),
                box = Rectangle(
                    left = o.Left,
                    right = o.Right,
                    top = o.Top,
                    bottom = o.Bottom,
                )
            )
        return list(map(convert, self.net.Detect(image))) # type: ignore
