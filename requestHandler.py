import threading
from motorDriver import motor
#import motorDriver

class requestHandle(object):
    #def __init__(self):
        #self.RAmotor = motor.RAmotor()
        #self.DECmotor = motor.DECmotor()
    
    def process(self, request):
        response = "None"
        if (request == None) or (request == ""): #Check if the client is disconnected without any notice
            response = "None"
        elif request == "Test":
            response = "OK"
        elif request == "Terminate":
            response = "Bye"
        elif request == "Quit":
            response == "Server closing"
        else:
            compon = request.split("_")
            if compon[0] == "TRNST":
                #self.RAmotor
                #Handle the transit function
                #Get the RA and DEC and convert to number, after that calculate the number of steps
                #ra_steps = float(compon[2])*num_of_stp_per_deg #Number of RA steps from home position
                #dec_steps = float(compon[4])*num_of_stp_per_deg #Number of DEC steps from home position
                #Read from the log the current position to calculate the true steps needed to reach the required point
                #Add a statement to check whether the motion is going to be to the left or to the right
                #After that call the appropriate function from the motor driver file and set the delay to the maximum possible speed
                #If RA is > 180 and < 0 or 360 then the motion will be to the right, otherwise to the left
                #Or maybe if the number of required steps is < 0 then determine the motion
                print("Received TR")
            elif compon[0] == "AAF":
                #Handle the aim and follow function
                print("Received AAF")
            elif compon[0] == "SCAN":
                #Handle the scan function
                print("Received SCAN")
            elif compon[0] == "SKYSCN":
                #Handle the sky scanning function
                print("Received SKYSCN")
        return response