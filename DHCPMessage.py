
class DHCPMessage():
  def __init__(self, data):
    self.op = data[0]
    self.htype = data[1]
    self.hlen = data[2]
    self.hops = data[3]
    self.xid = data[4:8]
    self.secs = data[8:10]
    self.flags = data[10:12]
    self.ciaddr = data[12:16]
    self.yiaddr = data[16:20]
    self.siaddr = data[20:24]
    self.giaddr = data[24:28]
    self.chaddr = data[28:44]
    self.sname = data[44:108]
    self.file = data[108:236]
    self.cookie = data[236:240]
    options = data[240:]
    end = False
    offset = 0
    while not end:
      code = options[offset]
      if code == 255:
        end = True
        
      length = options[offset+1]
      if length > 0:
        optiondata = options[offset+2:offset+2+int(length)]
        
      print("Code: {:d} Length: {:d}".format(code, length), optiondata)
      offset += length+2
