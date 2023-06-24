import jetson_inference # type: ignore
import jetson_utils     # type: ignore

DetectNet      = jetson_inference.detectNet
VideoSource    = jetson_utils.videoSource
VideoOutput    = jetson_utils.videoOutput
Image          = jetson_utils.cudaImage
DetectedObject = DetectNet.Detection
