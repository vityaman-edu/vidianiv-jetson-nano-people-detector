import jetson_inference
import jetson_utils

DetectNet      = jetson_inference.detectNet
VideoSource    = jetson_utils.videoSource
VideoOutput    = jetson_utils.videoOutput
Image          = jetson_utils.cudaImage
DetectedObject = DetectNet.Detection
