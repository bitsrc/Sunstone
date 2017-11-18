"""Sunstone

Begins the DHCP server process
"""
import SocketServer

from DHCPHandler import DHCPHandler


def main():
    """Begins a socketserver listening on port 67"""
#    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
#    s.bind(('', 67))
#    m = s.recvfrom(1024)
#    print(m)
    host, port = "", 67
    server = SocketServer.UDPServer((host, port), DHCPHandler)
    server.serve_forever()

if __name__ == "__main__":
    main()
