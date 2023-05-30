#!/usr/bin/env python3
import socket
import signal
import sys
import os
import time
import time
import base64
import imutils
import socket
import cv2

IP = "127.0.0.1"
PORT = 4242
BUFFER_SIZE = 65536
WIDTH = 400
SLEEP_BETWEEN_FRAMES = 0

def fprint(msg):
    print(msg, flush=True)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFFER_SIZE)

def notify(msg):
    msg_enc = msg.encode()
    # Send to controller using the address
    if client.send(msg_enc) != len(msg):
        print("ERROR SENDING MSG")

# Hook shutdown
def sigint_handler(sig, frame):
    client.close()
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

vid = cv2.VideoCapture(0)  #  replace 'rocket.mp4' with 0 for webcam

client.connect((IP, PORT))
print("Started equipment", flush=True)
while vid.isOpened():
    (_, frame) = vid.read()
    frame = imutils.resize(frame, width=WIDTH)
    (encoded, buffer) = cv2.imencode(".jpg", frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
    # Send to controller using the address
    client.send(base64.b64encode(buffer))
    time.sleep(SLEEP_BETWEEN_FRAMES)
