import io
import time
import picamera
import cv2
import numpy as np
import httplib
import json

try:
    import unicornhathd
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd

print("""Unicorn HAT HD: Emoji

Press Ctrl+C to exit!

""")

unicornhathd.rotation(0)

# Azure API Key
api_key = 'キー１'

# CV2
cascade_path = "/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml"

# Image Size
camera_width = 640
camera_height = 480

#####
def getEmotion(image, headers):
    try:
        conn = httplib.HTTPSConnection('api.projectoxford.ai')
        print "check3!"
        conn.request("POST", "/emotion/v1.0/recognize?", image, headers)
        print "check4!"
        response = conn.getresponse()
        print "check5!"
        data = response.read()
        print "check6!"
        conn.close()
        print "check7!"
        return data
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
        print(e.message)

def drawEmotion(data):
    data = json.loads(data)
    for face in data:
        f_rec  =  face['scores']
        f_rec = sorted(f_rec.items(), key=lambda x:x[1],reverse = True)
        emo = f_rec[0][0]

        R = np.load('rgb/' + emo + '_R.npy')
        G = np.load('rgb/' + emo + '_G.npy')
        B = np.load('rgb/' + emo + '_B.npy')
        for x in range(0, 16):
            for y in range(0, 16):
                unicornhathd.set_pixel(x, y, R[x][y], G[x][y], B[x][y])
        unicornhathd.show()
#####


try:
    while True:
        # Create the in-memory stream
        stream = io.BytesIO()
        with picamera.PiCamera() as camera:
            camera.resolution = (camera_width, camera_height)
            camera.capture(stream, format='jpeg')
        print "captured!"

        # Construct a numpy array from the stream
        data = np.fromstring(stream.getvalue(), dtype=np.uint8)
        # "Decode" the image from the array, preserving colour
        image = cv2.imdecode(data, 1)

        print "check1!"

        # Detect face
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cascade = cv2.CascadeClassifier(cascade_path)
        facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

        print "check2!"

        print "face rectangle"
        print facerect

        if len(facerect) > 0:
            save_file_name = "face_detect.jpg"

            cv2.imwrite(save_file_name, image)

            headers = {
                'Content-Type': 'application/octet-stream',
                'Ocp-Apim-Subscription-Key': api_key,
            }
            image_load = open(save_file_name, 'rb')
            data = getEmotion(image_load, headers)
            print data

            drawEmotion(data)

        else:
            R = np.load('rgb/no-face_R.npy')
            G = np.load('rgb/no-face_G.npy')
            B = np.load('rgb/no-face_B.npy')
            for x in range(0, 16):
                for y in range(0, 16):
                    unicornhathd.set_pixel(x, y, R[x][y], G[x][y], B[x][y])
            unicornhathd.show()

        sleep(1)
        print "."
        sleep(1)
        print "."
        sleep(1)
        print "."
        sleep(1)
        print "."
        sleep(1)
        print "."

except KeyboardInterrupt:
    unicornhathd.off()
