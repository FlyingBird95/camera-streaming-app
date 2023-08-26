from typing import Generator

import cv2
from flask import Response

from .blueprint import video_blueprint


def gen_frames() -> Generator[bytes, None, None]:
    """Return a generator of bytes, which encode the video contents.
    
    Copied from https://towardsdatascience.com/video-streaming-in-web-browsers-with-opencv-flask-93a38846fe00
    """
    camera = cv2.VideoCapture(0)  # 0 means local camera.
    
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            
            # concat frame one by one and show result
            yield b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'


@video_blueprint.get("/feed")
def feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
