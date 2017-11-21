import socket

class TCPServer(object):
    def __init__(self, cfg):
        self.client_connected = False
        self.port = cfg.getPort() #Get the server port from the settings file
        self.sock = self.createSocket()
    
    def createSocket(self):
        #Get hostname of the current machine
        sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sck.connect( ("8.8.8.8", 80) )
        hostname = sck.getsockname()[0] #Get the local ip returned
        sck.close()
        #hostname = socket.gethostname() #Get the hostname of the machine
        #hostname = "192.168.2.10"
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create a socket
        sock.bind((hostname, int(self.port))) #Bind to the socket
        sock.listen(1) #Set the listening to one connection
        return sock #Return the socket object
    
    def acceptConnection(self):
        self.client, claddr = self.sock.accept()
        self.client_connected = True
        return claddr
    
    def receive(self):
        if self.client_connected:
            return self.client.recv(1024).decode('utf-8')
        else:
            return ""
    
    def releaseClient(self):
        if self.client_connected:
            self.client.close()
            self.client_connected = False
        else:
            self.client_connected = False
        return self.client_connected
    
    def sendResponse(self, response):
        if self.client_connected:
            try:
                self.client.send(response.encode('utf-8'))
                return response
            except:
                return "Error in sending"