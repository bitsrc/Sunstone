import SocketServer

class DHCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = bytearray(self.request[0])
        socket = self.request[1]
        print(data)
        op = data[0]
        htype = data[1]
        hlen = data[2]
        hops = data[3]
        xid = data[4:8]
        secs = data[8:10]
        flags = data[10:12]
        ciaddr = data[12:16]
        yiaddr = data[16:20]
        siaddr = data[20:24]
        giaddr = data[24:28]
        chaddr = data[28:44]
        sname = data[44:108]
        file = data[108:236]
        options = data[236:]
        print(op,htype,hlen,hops,xid,secs,flags,ciaddr,yiaddr,siaddr,giaddr,chaddr,sname)