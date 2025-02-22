import cv2
import streamlit as st
from datetime import datetime

st.title("Motion Detector")
start = st. button('Start Camera')


if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:

        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Get current tme as a datetime object
        now = datetime.now()

        # Get day and time add them to the frame
        cv2.putText(img=frame, text=now.strftime("%A"), org=(30, 60),
                    fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=2,
                    color=(20, 100, 20),
                    thickness=2, lineType=cv2.LINE_AA)
        cv2.putText(img=frame, text=now.strftime("%H:%M:%M"), org=(30, 100),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, 
                    fontScale=2, 
                    color=(255, 0, 0),
                    thickness=2, lineType=cv2.LINE_AA)
        streamlit_image.image(frame)
