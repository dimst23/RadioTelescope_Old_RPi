import socket
import logData_Pi

class TCPServer(object):
    def __init__(self, cfg):
        self.client_connected = False
        self.port = cfg.getPort() #Get the server port from the settings file
        self.sock = self.createSocket()
        self.log_data = logData_Pi.logData(__name__)
    
    def createSocket(self):
        #Get hostname of the current machine
        sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sck.connect( ("8.8.8.8", 80) )
        hostname = sck.getsockname()[0] #Get the local IP returned
        sck.close() #Release the socket created for getting the local IP
        #hostname = socket.gethostname() #Get the hostname of the machine
        #hostname = "192.168.2.10"
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create a socket
        sock.bind((hostname, int(self.port))) #Bind to the socket
        sock.listen(1) #Set the listening to one connection
        return sock #Return the socket object
    
    def acceptConnection(self):
        try:
            self.client, claddr = self.sock.accept()
            self.client_connected = True
        except:
            self.log_data.log("EXCEPT", "An exception occurred while waiting for a client to connect")
            exit(1)
        else:
            return claddr, self.client_connected
    
    def receive(self):
        if self.client_connected:
            try:
                return self.client.recv(1024).decode('utf-8')
            except ConnectionResetError:
                self.log_data.log("EXCEPT", "A connected client abruptly disconnected. Returning to connection waiting")
                self.client_connected = False
                return ""
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
                self.log_data.log("EXCEPT", "There was an issue sending the response to the client")