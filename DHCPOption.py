import struct

CODE_SUBNET = 1
CODE_TIMEOFFSET = 2
CODE_ROUTER = 3
CODE_TIMESERVER = 4
CODE_NAMESERVER = 5
CODE_DNS = 6
CODE_LOGSERVER = 7
CODE_TYPE = 53
CODE_END = 255

TYPE_DISCOVER = 1
TYPE_OFFER = 2
TYPE_REQUEST = 3
TYPE_ACK = 5
TYPE_NAK = 6

class DHCPOption():
  def __init__(self, length, data):
    self.code = int(data[0])
    self.length = length
    self.data = data[2:]
  def text(self):
    return self.data
  def int(self):
    if len(self.data) == 1:
      return struct.unpack('B', self.data)[0]
    elif len(self.data) == 2:
      return struct.unpack('H', self.data)[0]
    elif len(self.data) == 4:
      return struct.unpack('L', self.data)[0]
  def ip(self):
    if len(self.data) == 4:
      octets = list(map(lambda x: int(x), self.data))
      return "{}.{}.{}.{}".format(octets[0],octets[1],octets[2],octets[3])
    else:
      return None