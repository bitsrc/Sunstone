import SocketServer
import DHCPMessage

class DHCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = bytearray(self.request[0])
        socket = self.request[1]
        
        msg = DHCPMessage.DHCPMessage(data)
        
        print(msg.op, msg.xid, msg.chaddr)