import time
import picamera
from PIL import Image

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    time.sleep(2)
    camera.capture('foo.jpg')

im = Image.open("foo.jpg")
im.show()
