import time
import socket
import sys
import os

from click import command
s = socket.socket()
host = "127.0.0.1"
port = 5665
s.connect((host, port))
command = s.recv(1024)
command = command.decode()
if command == "open":
    print("command is :", command)
    s.send("Command received".encode())
    os.system('ls')
