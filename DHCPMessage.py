import DHCPOption

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
    optiondata = data[240:]
    
    self.options = {}
    
    end = False
    offset = 0
    while not end:      
      length = int(optiondata[offset+1])
      
      option = DHCPOption.DHCPOption(length, optiondata[offset:offset+2+length])
      self.options[option.code] = option
      if option.code == 255:
        end = True

      offset += length+2

