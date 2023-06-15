from typing import List
from service import Recognizer
from jetson.video import ImageInput, ImageOutput
from jetson.inference import Detector
from model import Detection


def output_detected(objects: List[Detection]):
    if len(objects) == 0: return
    print('[JS] --- Detected Objects --- ')
    for object in objects:
        print(f'[JS] Detection with confidence {object.confidence:.2f}')
        print(f'[JS]   left:   {object.box.left:.2f}')
        print(f'[JS]   right:  {object.box.right:.2f}')
        print(f'[JS]   top:    {object.box.top:.2f}')
        print(f'[JS]   bottom: {object.box.bottom:.2f}')
        print()
    print('[JS] --- ---------------- --- ')
    print()
    print()


if __name__ == '__main__':
    Recognizer(
        model = Detector(Detector.Parameters(
            name = 'peoplenet',
            threshold = 0.3,
            tracking = Detector.Parameters.Tracking(
                min_frames = 3,
                drop_frames = 15,
                overlap_threshold = 0.5,
            )
        )),
        video_input = ImageInput('csi://0'),
        video_output = ImageOutput('rtp://192.168.1.40:1234'),
        objects_output = output_detected,
        config = Recognizer.Config(
            detection_period = 15,
        ),
    ).run()
