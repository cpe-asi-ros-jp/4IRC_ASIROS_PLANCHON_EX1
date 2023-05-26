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

def fprint(msg):
    print(msg, flush=True)

# Open a datagram socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFFER_SIZE)

def notify(data):
    # Send to controller using the address
    s.sendto(data, (IP, PORT))

# Hook shutdown
def sigint_handler(sig, frame):
    s.close()
    sys.exit(0)

vid = cv2.VideoCapture(0) #  replace 'rocket.mp4' with 0 for webcam
(video_fps, st, frames_to_count, cnt) = (0, 0, 20, 0)

while True:
	while vid.isOpened():
		(_, frame) = vid.read()
		frame = imutils.resize(frame, width = WIDTH)
		(encoded, buffer) = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
		message = base64.b64encode(buffer)
		s.sendto(message, client_addr)
		frame = cv2.putText(
            frame,
            'FPS: ' + str(video_fps),
            (10, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7, 
            (0, 0, 255),
            2
        )
		cv2.imshow('TRANSMITTING VIDEO', frame)
		key = cv2.waitKey(1) & 0xFF
		if key == ord('q'):
			s.close()
			break
		if cnt == frames_to_count:
			try:
				video_fps = round(frames_to_count / (time.time() - st))
				st = time.time()
				cnt = 0
			except:
				pass
		cnt+=1
