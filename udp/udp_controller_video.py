#!/usr/bin/env python3
import socket
import time
import cv2
import numpy as np
import signal
import sys
import base64

IP = "127.0.0.1"
PORT = 4242
BUFFER_SIZE = 65536

def fprint(msg):
    print(msg, flush=True)

# Open a datagram socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFFER_SIZE)

# Link to local machine on port 4242
s.bind((IP, PORT))
fprint("Controller listening on %s:%d" % (IP, PORT))

def on_sigint(sig, frame):
    s.close()
    sys.exit(0)
signal.signal(signal.SIGINT, on_sigint)

(video_fps, st, frames_to_count, cnt) = (0, 0, 20, 0)
while True:
	(packet, _) = s.recvfrom(BUFFER_SIZE)
	data = base64.b64decode(packet, ' /')
	numpy_data = np.fromstring(data, dtype=np.uint8)
	frame = cv2.imdecode(numpy_data, 1)
	frame = cv2.putText(
        frame,
        'FPS: ' + str(video_fps),
        (10,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 255),
        2
    )
	cv2.imshow("RECEIVING VIDEO", frame)
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
	cnt += 1
