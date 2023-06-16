from enum import Enum


class Codec(Enum):
    H264  = 'h264'
    H265  = 'h265'
    VP8   = 'vp8'
    VP9   = 'vp9'
    MPEG2 = 'mpeg2'
    MPEG4 = 'mpeg4'
    MJPEG = 'mjpeg'
