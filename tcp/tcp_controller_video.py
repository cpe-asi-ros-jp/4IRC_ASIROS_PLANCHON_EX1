#!/usr/bin/env python3
import socket
import sys
import signal
import socket
import time
import cv2
import numpy as np
import base64

IP = "127.0.0.1"
PORT = 4242
BUFFER_SIZE = 65536

def fprint(msg):
    print(msg, flush=True)


# Open a datagram socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFFER_SIZE)

# Link to local machine on port 4242
s.bind((IP, PORT))
fprint("Controller listening on %s:%d" % (IP, PORT))

last_client = None
def on_sigint(sig, frame):
    s.close()
    if last_client != None: last_client.close()
    sys.exit(0)


signal.signal(signal.SIGINT, on_sigint)

(video_fps, st, frames_to_count, cnt) = (0, 0, 20, 0)
while True:
    s.listen(1)
    (client, (client_ip, client_port)) = s.accept()
    last_client = client
    packet = client.recv(BUFFER_SIZE)
    data = base64.b64decode(packet, " /")
    numpy_data = np.frombuffer(data, dtype=np.uint8)
    frame = cv2.imdecode(numpy_data, 1)
    frame = cv2.putText(
        frame,
        "FPS: " + str(video_fps),
        (10, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2,
    )
    cv2.imshow("CONTROLLER", frame)
    key = cv2.waitKey(1) & 0xFF
    if cnt == frames_to_count:
        try:
            video_fps = round(frames_to_count / (time.time() - st))
            st = time.time()
            cnt = 0
        except:
            pass
    cnt += 1

