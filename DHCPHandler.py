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

    if type == DHCPOption.TYPE_DISCOVER:
      # Looking for a DHCP server
      print("DHCP Discovery")
      self.dhcpserver.handleDiscover(msg)
    elif type == DHCPOption.TYPE_OFFER:
      # If we're the server, we shouldn't see this as we will send
      print("DHCP Offer")
      #self.dhcpserver.handleOffer(msg)
    elif type == DHCPOption.TYPE_REQUEST:
      # Accepting an address and requesting it be confirmed
      print("DHCP Request")
      self.dhcpserver.handleRequest(msg)
    elif type == DHCPOption.TYPE_DECLINE:
      # Client declining an address
      print("DHCP Decline")
      self.dhcpserver.handleDecline(msg)
    elif type == DHCPOption.TYPE_ACK:
      # Again, we send this, but this confirms the acceptance of an address
      print("DHCP Ack")
      #self.dhcpserver.handleAck(msg)
    elif type == DHCPOption.TYPE_NAK:
      # We would send this if anything, but this would deny the acceptance of an address
      print("DHCP Nak")
      #self.dhcpserver.handleNak(msg)
    elif type == DHCPOption.TYPE_RELEASE:
      # Client releasing their address
      print("DHCP Release")
      self.dhcpserver.handleRelease(msg)
    elif type == DHCPOption.TYPE_INFORM:
      # Client requesting local config info while already having an address
      print("DHCP Inform")
      self.dhcpserver.handleInform(msg)