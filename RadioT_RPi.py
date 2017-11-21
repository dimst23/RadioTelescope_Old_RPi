#!/usr/bin/env python3.5

#Import the required libraries and classes
from TCPServer import TCPServer
from configData_Pi import confDataPi
from requestHandler import requestHandle
from motorDriver import motor

def main():
    cfg = confDataPi("settings_pi.xml")
    server = TCPServer(cfg)
    request_hndl = requestHandle()
    con_client = False
    result = "none"
    
    motor.GPIOInit() #Initialize the GPIO pins on the Raspberry
    
    while(True):
        if con_client == False:
            cl_addr = server.acceptConnection()
            print("Connection request accepted")
            print("Connected with %s:%s" %(cl_addr[0], cl_addr[1]))
            con_client = True
        request = server.receive() #Wait until you receive a request from the client
        result = request_hndl.process(request) #Pass the received request to the request handler and get the response from the handler
        server.sendResponse(result) #Send the response from the handler to the client
        
        if result == "Bye":
            #Some more code needed to handle step count saving etc
            server.releaseClient()
            con_client = False
            print("Client %s:%s released after request" %(cl_addr[0], cl_addr[1]))
            continue
        elif result == "Server closing":
            #Some more code needed to handle step count saving etc
            server.releaseClient()
            print("Client %s:%s released after request" %(cl_addr[0], cl_addr[1]))
            print("Server is terminating after client's request")
            break

if __name__  == '__main__':
    main()