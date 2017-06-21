#!/usr/bin/python

import sys, posix, time, md5, binascii, socket, select

class ApiRos:
    "Routeros api"
    def __init__(self, sk):
        self.sk = sk
        self.currenttag = 0
        
    def login(self, username, pwd):
        for repl, attrs in self.talk(["/login"]):
            chal = binascii.unhexlify(attrs['=ret'])
        md = md5.new()
        md.update('\x00')
        md.update(pwd)
        md.update(chal)
        self.talk(["/login", "=name=" + username,
                   "=response=00" + binascii.hexlify(md.digest())])
       
    def talk(self, words):
        if self.writeSentence(words) == 0: return
        r = []
        while 1:
            i = self.readSentence();
            if len(i) == 0: continue
            reply = i[0]
            attrs = {}
            for w in i[1:]:
                j = w.find('=', 1)
                if (j == -1):
                    attrs[w] = ''
                else:
                    attrs[w[:j]] = w[j+1:]
            r.append((reply, attrs))
            if reply == '!done': return r

    def writeSentence(self, words):
        ret = 0
        for w in words:
            self.writeWord(w)
            ret += 1
        self.writeWord('')
        return ret

    def readSentence(self):
        r = []
        while 1:
            w = self.readWord()
            if w == '': return r
            r.append(w)
            
    def writeWord(self, w):
        print "<<< " + w
        self.writeLen(len(w))
        self.writeStr(w)

    def readWord(self):
        ret = self.readStr(self.readLen())
        print ">>> " + ret
        return ret

    def writeLen(self, l):
        if l < 0x80:
            self.writeStr(chr(l))
        elif l < 0x4000:
            l |= 0x8000
            self.writeStr(chr((l >> 8) & 0xFF))
            self.writeStr(chr(l & 0xFF))
        elif l < 0x200000:
            l |= 0xC00000
            self.writeStr(chr((l >> 16) & 0xFF))
            self.writeStr(chr((l >> 8) & 0xFF))
            self.writeStr(chr(l & 0xFF))
        elif l < 0x10000000:        
            l |= 0xE0000000         
            self.writeStr(chr((l >> 24) & 0xFF))
            self.writeStr(chr((l >> 16) & 0xFF))
            self.writeStr(chr((l >> 8) & 0xFF))
            self.writeStr(chr(l & 0xFF))
        else:                       
            self.writeStr(chr(0xF0))
            self.writeStr(chr((l >> 24) & 0xFF))
            self.writeStr(chr((l >> 16) & 0xFF))
            self.writeStr(chr((l >> 8) & 0xFF))
            self.writeStr(chr(l & 0xFF))

    def readLen(self):              
        c = ord(self.readStr(1))    
        if (c & 0x80) == 0x00:      
            pass                    
        elif (c & 0xC0) == 0x80:    
            c &= ~0xC0              
            c <<= 8                 
            c += ord(self.readStr(1))    
        elif (c & 0xE0) == 0xC0:    
            c &= ~0xE0              
            c <<= 8                 
            c += ord(self.readStr(1))    
            c <<= 8                 
            c += ord(self.readStr(1))    
        elif (c & 0xF0) == 0xE0:    
            c &= ~0xF0              
            c <<= 8                 
            c += ord(self.readStr(1))    
            c <<= 8                 
            c += ord(self.readStr(1))    
            c <<= 8                 
            c += ord(self.readStr(1))    
        elif (c & 0xF8) == 0xF0:    
            c = ord(self.readStr(1))     
            c <<= 8                 
            c += ord(self.readStr(1))    
            c <<= 8                 
            c += ord(self.readStr(1))    
            c <<= 8                 
            c += ord(self.readStr(1))    
        return c                    

    def writeStr(self, str):        
        n = 0;                      
        while n < len(str):         
            r = self.sk.send(str[n:])
            if r == 0: raise RuntimeError, "connection closed by remote end"
            n += r                  

    def readStr(self, length):      
        ret = ''                    
        while len(ret) < length:    
            s = self.sk.recv(length - len(ret))
            if s == '': raise RuntimeError, "connection closed by remote end"
            ret += s
        return ret

#IP ROUTE
    def addRoute(self, dst, src, gateway):
        self.inputsentence = ["/ip/route/add"]
        self.inputsentence.append("=dst-address=" + dst)
	self.inputsentence.append("=pref-src=" + src)
        self.inputsentence.append("=gateway=" + gateway)
        self.writeSentence(self.inputsentence)
        self.readSentence()

    def printRoute(self):
        self.inputsentence = ["/ip/route/print"]
	self.inputsentence.append("=count-only=")
        self.writeSentence(self.inputsentence)
	count = int(self.readSentence()[1][5:])

	number = 0
	while (number <= count):
		self.inputsentence = ["/ip/route/print"]
		print "No. " + str(number)
		self.writeSentence(self.inputsentence)
		self.readSentence()
		number= number+1

    def deleteRoute(self, number):
        self.inputsentence = ['/ip/route/remove']
        self.inputsentence.append('=numbers=' + number)
        self.writeSentence(self.inputsentence)
        self.readSentence()

    def updateRoute(self, number, dst, source, gateway):
	self.inputsentence = ["/ip/route/set"]
	self.inputsentence.append("=numbers=" + number)
	self.inputsentence.append("=dst-address=" + dst)
	self.inputsentence.append("=pref-src=" + source)
	self.inputsentence.append("=gateway=" + gateway)
	self.writeSentence(self.inputsentence)
	self.readSentence()

#IPSEC PEER
    def addPeer(self, addr, port, secret):
        self.inputsentence = ["/ip/ipsec/peer/add"]
        self.inputsentence.append("=address=" + addr)
	self.inputsentence.append("=port=" + port)
        self.inputsentence.append("=auth-method=pre-shared-key")
	self.inputsentence.append("=secret=" + secret)
        self.writeSentence(self.inputsentence)
        self.readSentence()

    def printPeer(self):
        self.inputsentence = ["/ip/ipsec/peer/print"]
	self.inputsentence.append("=count-only=")
        self.writeSentence(self.inputsentence)
	count = int(self.readSentence()[1][5:])

	number = 0
	while (number <= count):
		self.inputsentence = ["/ip/ipsec/peer/print"]
		print "No. #" + str(number)
		self.writeSentence(self.inputsentence)
		self.readSentence()
		number= number+1

    def deletePeer(self, number):
        self.inputsentence = ['/ip/ipsec/peer/remove']
        self.inputsentence.append('=numbers=' + number)
        self.writeSentence(self.inputsentence)
        self.readSentence()

    def updatePeer(self, number, addr, port, secret):
	self.inputsentence = ["/ip/ipsec/peer/set"]
	self.inputsentence.append("=numbers=" + number)
	self.inputsentence.append("=address=" + addr)
	self.inputsentence.append("=port=" + port)
	self.inputsentence.append("=secret=" + secret)
	self.writeSentence(self.inputsentence)
	self.readSentence()

#IPSEC POLICY
    def addPolicy(self, srcaddr, srcport, dstaddr, dstport, sasrcaddr, sadstaddr, tunnel, action, proposal):
        self.inputsentence = ["/ip/ipsec/policy/add"]
        self.inputsentence.append("=src-address=" + srcaddr)
	self.inputsentence.append("=src-port=" + srcport)
        self.inputsentence.append("=dst-address=" + dstaddr)
	self.inputsentence.append("=dst-port=" + dstport)
	self.inputsentence.append("=sa-src-address=" + sasrcaddr)
	self.inputsentence.append("=sa-dst-address=" + sadstaddr)
	self.inputsentence.append("=tunnel=" + tunnel)
	self.inputsentence.append("=action=" + action)
	self.inputsentence.append("=proposal=" + proposal)
        self.writeSentence(self.inputsentence)
        self.readSentence()

    def printPolicy(self):
        self.inputsentence = ["/ip/ipsec/policy/print"]
	self.inputsentence.append("=count-only=")
        self.writeSentence(self.inputsentence)
	count = int(self.readSentence()[1][5:])

	number = 0
	while (number <= count):
		self.inputsentence = ["/ip/ipsec/policy/print"]
		print "No. #" + str(number)
		self.writeSentence(self.inputsentence)
		self.readSentence()
		number= number+1

    def deletePolicy(self, number):
        self.inputsentence = ['/ip/ipsec/policy/remove']
        self.inputsentence.append('=numbers=' + number)
        self.writeSentence(self.inputsentence)
        self.readSentence()

    def updatePolicy(self, number, srcaddr, srcport, dstaddr, dstport, sasrcaddr, sadstaddr, tunnel, action, proposal):
	self.inputsentence = ["/ip/ipsec/policy/set"]
	self.inputsentence.append("=numbers=" + number)
	self.inputsentence.append("=src-address=" + srcaddr)
	self.inputsentence.append("=src-port=" + srcport)
        self.inputsentence.append("=dst-address=" + dstaddr)
	self.inputsentence.append("=dst-port=" + dstport)
	self.inputsentence.append("=sa-src-address=" + sasrcaddr)
	self.inputsentence.append("=sa-dst-address=" + sadstaddr)
	self.inputsentence.append("=tunnel=" + tunnel)
	self.inputsentence.append("=action=" + action)
	self.inputsentence.append("=proposal=" + proposal)
        self.writeSentence(self.inputsentence)
        self.readSentence()

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('20.20.20.1', 8728))  
    apiros = ApiRos(s);             
    apiros.login('admin', '');
    
    #IP ROUTE
    if sys.argv[1] == "printRoute":
	apiros.printRoute();
    elif sys.argv[1] == "createRoute":
	apiros.addRoute(sys.argv[2], sys.argv[3], sys.argv[4]);
    elif sys.argv[1] == "updateRoute":
	apiros.updateRoute(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]);
    elif sys.argv[1] == "deleteRoute":
	apiros.deleteRoute(sys.argv[2]);
    #IPSEC PEER
    elif sys.argv[1] == "printPeer":
	apiros.printPeer();
    elif sys.argv[1] == "createPeer":
	apiros.addPeer(sys.argv[2], sys.argv[3], sys.argv[4]);
    elif sys.argv[1] == "updatePeer":
	apiros.updatePeer(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]);
    elif sys.argv[1] == "deletePeer":
	apiros.deletePeer(sys.argv[2]);
    #IPSEC POLICY
    elif sys.argv[1] == "printPolicy":
	apiros.printPolicy();
    elif sys.argv[1] == "createPolicy":
	apiros.addPolicy(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10]);
    elif sys.argv[1] == "updatePolicy":
	apiros.updatePolicy(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10], sys.argv[11]);
    elif sys.argv[1] == "deletePolicy":
	apiros.deletePolicy(sys.argv[2]);

if __name__ == '__main__':
	main()
