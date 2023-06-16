from typing import Collection, List, Union, Dict, Any
from .reciever import Reciever
from jetson.inference.detection import Detection
import socket
import sys
import json

class SocketReciever(Reciever):
    def __init__(self, host: str, port: int, debug = False) -> None:
        self.host = host
        self.port = port
        self.debug = True
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def take(self, detected_objects: Collection[Detection]) -> Collection[Detection]:
        json_str = json.dumps(self.jsones_from(detected_objects))
        self.sock.sendto(bytes(json_str, encoding='utf-8'), (self.host, self.port))
        if self.debug and len(detected_objects) > 0: 
            print(f'[JS] Send: {json_str}') # TODO: debug logging 
        return detected_objects

    def jsones_from(self, objects: Collection[Detection]) -> List[Dict[str, Any]]:
        return [self.json_from(o) for o in objects]
    
    def json_from(self, object: Detection) -> Dict[str, Any]:
        return {
            'label': object.kind.label,
            'conf': object.confidence,
            'box': {
                'left': object.box.left,
                'right': object.box.right,
                'top': object.box.top,
                'bottom': object.box.bottom,
            },
        }