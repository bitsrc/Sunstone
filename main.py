import os
import socket
import sys
import SocketServer

from DHCPHandler import DHCPHandler


def main():
#    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
#    s.bind(('', 67))
#    m = s.recvfrom(1024)
#    print(m)
    HOST, PORT = "", 67
    server = SocketServer.UDPServer((HOST, PORT), DHCPHandler)
    server.serve_forever()

if __name__ == "__main__":
    main()