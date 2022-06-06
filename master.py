from audioop import add
import time
import socket
import sys
import os

from click import command
s = socket.socket()
host = socket.gethostname()
port = 5665
s.blind(('', port))
s.listen()
conn, addr = s.accept()
print(addr,"is connected to server")
command = input(str("Enter command :"))
conn.send(command.encode())
print("Command has been sent successfully")
data = conn.rev(1024)
if data:
    print("Command received and executed successfully.")
