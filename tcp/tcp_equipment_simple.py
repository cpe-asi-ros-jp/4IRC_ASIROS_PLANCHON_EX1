#!/usr/bin/env python3
import socket
import signal
import sys
import os
import time

IP = "127.0.0.1"
PORT = 4242
BUFFER_SIZE = 1024


def fprint(msg):
    print(msg, flush=True)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def notify(msg):
    msg_enc = msg.encode()
    # Send to controller using the address
    if client.send(msg_enc) != len(msg):
        print("ERROR SENDING MSG")

# Hook shutdown
def sigint_handler(n=False):
    if n:
        notify("off")
        client.close()
    sys.exit(0)

# Create alive subprocess
pid = os.fork()
if pid == 0:
    signal.signal(signal.SIGINT, lambda sig, frame: sigint_handler(False))
    while True:
        time.sleep(5)
        notify("alive")
else:
    signal.signal(signal.SIGINT, lambda sig, frame: sigint_handler(True))
    client.connect((IP, PORT))
    notify("on")
    while True:
        fprint("Press a button? [y/n] (CTRL-C to quit)")
        press_btn = input()
        if press_btn.lower() == "y":
            notify("button pressed")
