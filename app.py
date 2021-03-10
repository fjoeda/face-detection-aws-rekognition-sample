# This is the simple example for face detection using AWS Rekognition and OpenCV
# Simplified by fjoeda


import cv2
import numpy as np
import boto3

# The access to AWS Rekognition can be obtained through AWS Credentials you can get from AWS Educate Vocaerum labs
# You need to change this credentials below with the one that you get from AWS Educate Account
client = boto3.client("rekognition",
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        aws_session_token=SESSION_TOKEN
    )


# function to extract face features
def detect_face(photo):
    
    response = client.detect_faces(
        Image={
            'Bytes': photo
        }, 
        Attributes=[
            'ALL'
        ]
    )
    return response

# variables for capturing the image using webcam
cam = cv2.VideoCapture(0)

#the main loop
while True:
    # read the frame from webcam
    ret, frame = cam.read()
    # show the frame in a window
    cv2.imshow("frame",frame)

    # handles for input keys
    k = cv2.waitKey(1)

    # detect if escape key is pressed
    if k%256 == 27:
        # stop the code
        break
    # detect if space key is pressed
    elif k%256 == 32:
        # send frame for face detection by AWS Rekognition
        print(detect_face(cv2.imencode('.jpg', frame)[1].tostring()))

# turning off the camera and close all windows
cam.release()
cv2.destroyAllWindows()
