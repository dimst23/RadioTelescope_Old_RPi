#!/usr/bin/env python3.5

#Import the required libraries and classes
import TCPServer
import configData_Pi
import requestHandler
import motorDriver 

def main():
    cfg = configData_Pi.confDataPi("settings_pi.xml")
    server = TCPServer.TCPServer(cfg)
    request_hndl = requestHandler.requestHandle()
    motor = motorDriver.motor()
    con_client = False
    result = "none"
    
    motor.GPIO_Init() #Initialize the GPIO pins on the Raspberry
    
    while(True):
        if con_client == False:
            cl_addr = server.acceptConnection()
            print("Connection request accepted")
            print("Connected with %s:%s" %(cl_addr[0], cl_addr[1]))
            con_client = True
        request = server.receive() #Wait until you receive a request from the client
        result = request_hndl.process(request, cfg) #Pass the received request to the request handler and get the response from the handler
        server.sendResponse(result) #Send the response from the handler to the client
        
        if result == "Bye":
            #Some more code needed to handle step count saving etc
            server.releaseClient()
            con_client = False
            print("Client %s:%s released after request" %(cl_addr[0], cl_addr[1]))
            continue
        elif result == "None":
            server.releaseClient()
            con_client = False
            print("Client %s:%s exited without notice" %(cl_addr[0], cl_addr[1]))
            continue
        elif result == "Server closing":
            #Some more code needed to handle step count saving etc
            server.releaseClient()
            print("Client %s:%s released after request" %(cl_addr[0], cl_addr[1]))
            print("Server is terminating after client's request")
            exit(0)

if __name__  == '__main__':
    main()