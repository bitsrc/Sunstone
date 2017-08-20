import DHCPMessage

class DHCPServer():
  def handleDiscover(self, msg):
    print("DHCP Discover from {}".format(msg.clientAddress()))
    