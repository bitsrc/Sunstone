import DHCPMessage

class DHCPServer():
  def handleDiscover(self, msg):
    # Determine an address, put a hold on it, send an offer
    print("DHCP Discover from {}".format(msg.clientAddress()))

  def handleRequest(self, msg):
    # Verify it is our offer, store the lease, send an ACK
    pass

  def handleDecline(self, msg):
    # Remove hold
    pass

  def handleRelease(self, msg):
    # Mark lease as inactive?
    pass

  def handleInform(self, msg):
    # Send ACK
    pass

  # Unused, these are messages we generate
  def handleOffer(self, msg):
    pass
  def handleAck(self, msg):
    pass
  def handleNak(self, msg):
    pass