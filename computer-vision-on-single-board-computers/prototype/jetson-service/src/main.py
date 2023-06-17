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
from service.reciever import (
    Deduplicator,
    ConsoleReciever, 
    SocketReciever,
    SequenceReciever,
)
from argv import Arguments


if __name__ == '__main__':
    args = Arguments.parse_argv()
    Recognizer(
        model = Detector(DetectorParameters(
            name = ModelName.PEOPLENET,
            threshold = 0.4,
            # tracking = TrackingParameters(
            #     min_frames = 3,
            #     drop_frames = 15,
            #     overlap_threshold = 0.5,
            # ),
        )),
        video_input = ImageInput('csi://0', ImageInputParameters(
            width = 640, 
            height = 380,
            framerate = 20,
            codec = Codec.H264,
            flip = True,
        )),
        video_output = ImageOutput(f'rtsp://@:1234/output', ImageOutputParameters(
            codec = Codec.H264,
            bitrate = 300_000,
        )),
        reciever = SequenceReciever([
            Deduplicator(
                overlap_threshold = 0.5,
            ),
            # ConsoleReciever(
            #     tag = 'JS',
            #     sep = '=',
            #     verbose = True,
            # ),
            SocketReciever(
                host  = str(args.output.split(':')[0]), 
                port  = int(args.output.split(':')[1]),
                debug = False
            ),
        ]),
        config = RecognizerConfig(
            detection_period = 10,
        ),
    ).run()
