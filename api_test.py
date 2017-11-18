import io
import time
import picamera
import cv2
import numpy as np
import httplib
import json

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
        conn.request("POST", "/emotion/v1.0/recognize?", image, headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return data
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
        print(e.message)

def drawEmotion(image, data):
    font = cv2.FONT_HERSHEY_PLAIN
    font_size = 1
    data = json.loads(data)
    for face in data:
        f_rec  =  face['faceRectangle']
        width  =  f_rec['width']
        height =  f_rec['height']
        left   =  f_rec['left']
        top    =  f_rec['top']
        f_rec  =  face['scores']
        f_rec = sorted(f_rec.items(), key=lambda x:x[1],reverse = True)
        cv2.rectangle(image, (left,         top), (left + width,       top + height), (130, 130, 130), 3)
        cv2.rectangle(image, (left + width, top), (left + width + 150, top + 50),     (130, 130, 130), -1)

        for i in range(0, 5):
            val = round(f_rec[i][1], 3)
            emo = f_rec[i][0]
            cv2.rectangle(image, (left + width, top + 10 * i), (left + width + int(val * 150), top + 10 * (i + 1)),
                (180, 180, 180), -1)
            cv2.putText(image, emo + " " + str(val), (left + width, top + 10 * (i + 1)),
                font, font_size, (255,255,255), 1)
#####

# Create the in-memory stream
stream = io.BytesIO()
with picamera.PiCamera() as camera:
    camera.resolution = (camera_width, camera_height)
    camera.start_preview()
    time.sleep(0.5)
    camera.capture(stream, format='jpeg')

# Construct a numpy array from the stream
data = np.fromstring(stream.getvalue(), dtype=np.uint8)
# "Decode" the image from the array, preserving colour
image = cv2.imdecode(data, 1)

# Detect face
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cascade = cv2.CascadeClassifier(cascade_path)
facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

print "face rectangle"
print facerect

if len(facerect) > 0:
    save_file_name = "face_detect.jpg"
    save_emotion_file_name = "face_emotion.jpg"

    cv2.imwrite(save_file_name, image)

    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': api_key,
    }
    image_load = open(save_file_name, 'rb')
    data = getEmotion(image_load, headers)
    print data

    drawEmotion(image, data)
    cv2.imwrite(save_emotion_file_name, image)
