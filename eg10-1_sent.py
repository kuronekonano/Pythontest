import socket
import sys
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto(sys.argv[1].encode(),("10.51.226.128",5000))
s.close()