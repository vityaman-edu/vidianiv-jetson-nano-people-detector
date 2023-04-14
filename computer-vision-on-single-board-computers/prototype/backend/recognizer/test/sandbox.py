from vidianiv_people_recognizer import (
    Pipeline,
    CVVideoCapture,
    CV2VideoPreprocessor,
    YOLOV8Recognizer,
    CVDisplay
)

if __name__ == '__main__':
    pipeline = Pipeline(
        source=CVVideoCapture(0),
        preprocessor=CV2VideoPreprocessor(),
        recognizer=YOLOV8Recognizer(),
        consumer=CVDisplay('Sandbox')
    )
    pipeline.start()
