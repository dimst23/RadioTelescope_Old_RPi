#Import the required libraries and classes
from TCPServer import TCPServer
from configData_Pi import confDataPi
from requestHandler import requestHandle

def main():
    cfg = confDataPi("settings_pi.xml")
    server = TCPServer(cfg)
    request_hndl = requestHandle()
    con_client = False
    
    while(True):
        if con_client == False:
            server.acceptConnection()
            print("Conn accept")
            con_client = True
        request = server.receive() #Wait until you receive a request from the client
        result = request_hndl.process(request) #Pass the received request to the request handler and get the response from the handler
        server.sendResponse(result) #Send the response from the handler to the client
        
        if result == "Bye":
            server.releaseClient()
            con_client = False
            continue

if __name__  == '__main__':
    main()