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
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Link to local machine on port 4242
s.bind((IP, PORT))
fprint("Controller listening on %s:%d" % (IP, PORT))

last_client = None
def on_sigint(sig, frame):
    s.close()
    if last_client != None: last_client.close()
    sys.exit(0)


signal.signal(signal.SIGINT, on_sigint)

# Listen to incoming requests
while True:
    s.listen(1)
    (client, (client_ip, client_port)) = s.accept()
    last_client = client
    fprint("Client %s:%s connected" % (client_ip, client_port))
    data = client.recv(1024)
    while data:
        print("  Client sent %s" % data.decode(), flush=True)
        data = client.recv(1024)
