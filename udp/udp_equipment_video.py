#!/usr/bin/env python3
import numpy as np
import time
import base64
import imutils
import socket
import cv2
import signal
import sys

IP = "127.0.0.1"
PORT = 4242
BUFFER_SIZE = 65536
WIDTH = 400
SLEEP_BETWEEN_FRAMES = 0

# Open a datagram socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFFER_SIZE)


# Hook shutdown
def sigint_handler(sig, frame):
    s.close()
    sys.exit(0)


signal.signal(signal.SIGINT, sigint_handler)

vid = cv2.VideoCapture(0)  #  replace 'rocket.mp4' with 0 for webcam

print("Started equipment", flush=True)
while vid.isOpened():
    (_, frame) = vid.read()
    frame = imutils.resize(frame, width=WIDTH)
    (encoded, buffer) = cv2.imencode(".jpg", frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
    # Send to controller using the address
    s.sendto(base64.b64encode(buffer), (IP, PORT))
    time.sleep(SLEEP_BETWEEN_FRAMES)
