#!/usr/bin/env python3
import socket
import sys
import signal

IP = "127.0.0.1"
PORT = 4242
BUFFER_SIZE = 1024

def fprint(msg):
    print(msg, flush=True)

# Open a datagram socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Link to local machine on port 4242
s.bind((IP, PORT))
fprint("Controller listening on %s:%d" % (IP, PORT))

def on_sigint(sig, frame):
    s.close()
    sys.exit(0)
signal.signal(signal.SIGINT, on_sigint)


# Listen to incoming requests
while(True):
    (message, (client_ip, client_port)) = s.recvfrom(BUFFER_SIZE)
    fprint("Client %s:%s sent '%s'" % (client_ip, client_port, bytes.decode(message)))