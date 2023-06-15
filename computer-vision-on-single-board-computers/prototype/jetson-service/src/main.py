from service import Recognizer
from jetson.video import ImageInput, ImageOutput
from jetson.inference import Detector


if __name__ == '__main__':
    Recognizer(
        model = Detector(Detector.Parameters(
            name = "peoplenet",
            threshold = 0.3,
            tracking = Detector.Parameters.Tracking(
                min_frames = 3,
                drop_frames = 15,
                overlap_threshold = 0.5,
            )
        )),
        input = ImageInput("csi://0"),
        output = ImageOutput("rtp://192.168.1.40:1234")
    ).run()
