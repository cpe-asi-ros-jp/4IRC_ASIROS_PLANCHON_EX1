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


# Open a datagram soket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def notify(msg):
    # Send to controller using the address
    s.sendto(str.encode(msg), (IP, PORT))


# Hook shutdown
def sigint_handler(sig, frame):
    notify("off")
    sys.exit(0)


# Create alive subprocess
pid = os.fork()
if pid == 0:
    signal.signal(signal.SIGINT, lambda sig, frame: sys.exit(0))
    while True:
        time.sleep(5)
        notify("alive")
else:
    signal.signal(signal.SIGINT, sigint_handler)
    notify("on")
    while True:
        fprint("Press a button? [y/n] (CTRL-C to quit)")
        press_btn = input()
        if press_btn.lower() == "y":
            notify("button pressed")
