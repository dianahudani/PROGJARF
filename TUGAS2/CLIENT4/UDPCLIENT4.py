import socket
import base64
import os
import sys
import glob

TARGET_IP = '127.0.0.1'
TARGET_PORT = 9000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Connect Server
sock.sendto('CONNECTED',(TARGET_IP, TARGET_PORT))
print "Connecting to Server", TARGET_IP, TARGET_PORT

#Receive Server Response
data, addr = sock.recvfrom(1024)
if data == "CONNECTED":
    print "Connected to", addr

while True:
    data, addr = sock.recvfrom(1024)
    if data == "START":
        IMAGENAME, addr = sock.recvfrom(1024)
        print "Download", IMAGENAME
        fp = open(IMAGENAME,'wb+')
        terimadata=""
        while True:
            data, addr = sock.recvfrom(1024)
            terimadata+=data
            if data=="FINISH":
                break
        fp.write(terimadata)
        fp.close()
        print "Download Success"
            

sys.exit()