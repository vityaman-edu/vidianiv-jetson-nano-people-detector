from jetson.video import (
    ImageInput, 
    ImageOutput, 
    ImageInputParameters, 
    ImageOutputParameters,
    Codec,
)
from jetson.inference import (
    Detector, 
    DetectorParameters, 
    TrackingParameters,
    ModelName,
    Overlay,
)
from service.recognizer import Recognizer, RecognizerConfig
from service.reporter import ConsoleReporter
from argv import Arguments


if __name__ == '__main__':
    args = Arguments.parse_argv()
    Recognizer(
        model = Detector(DetectorParameters(
            name = ModelName.PEOPLENET,
            threshold = 0.5,
            tracking = TrackingParameters(
                min_frames = 3,
                drop_frames = 15,
                overlap_threshold = 0.5,
            ),
            overlay = { Overlay.BOX, Overlay.LABEL, Overlay.LABEL },
        )),
        video_input = ImageInput('csi://0', ImageInputParameters(
            width = 500, 
            height = 500,
            framerate = 30,
            codec = Codec.H264,
            flip = True,
        )),
        video_output = ImageOutput(args.output, ImageOutputParameters(
            codec = Codec.H264,
            bitrate = 4_000_000,
        )),
        reporter = ConsoleReporter(
            tag = 'JS',
            sep = '=',
            verbose = True,
            area_threshold = 0.8,
        ),
        config = RecognizerConfig(
            detection_period = 5,
        ),
    ).run()
