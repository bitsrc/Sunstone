import SocketServer
import DHCPMessage
import DHCPServer
import DHCPOption


class DHCPHandler(SocketServer.BaseRequestHandler):
    dhcpserver = DHCPServer.DHCPServer()
    def handle(self):
        data = bytearray(self.request[0])
        socket = self.request[1]
        
        msg = DHCPMessage.DHCPMessage(data)
        type = msg.options[DHCPOption.CODE_TYPE].int()
        print("DHCP Message: {}".format(type))
        if type == DHCPOption.TYPE_DISCOVER:
          print("DHCP Discovery")
          self.dhcpserver.handleDiscover(msg)
          