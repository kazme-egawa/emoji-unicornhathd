import time
import picamera
from PIL import Image

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.capture('foo.jpg')
