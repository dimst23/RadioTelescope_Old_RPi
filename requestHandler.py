import threading
import motorDriver

_steps_from_zero = 0 #Number of steps from true south and home position
num_of_stp_per_deg_ra = 100
num_of_stp_per_deg_dec = 430

class requestHandle(object):
    def __init__(self):
        self.motor = motorDriver.motor()
        #self.DECmotor = motor.DECmotor()
    
    def process(self, request, cfg_data):
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
                '''
                    #self.RAmotor
                    #Handle the transit function
                    #Get the RA and DEC and convert to number, after that calculate the number of steps
                    #Read from the log the current position to calculate the true steps needed to reach the required point
                    #Add a statement to check whether the motion is going to be to the left or to the right
                    #After that call the appropriate function from the motor driver file and set the delay to the maximum possible speed
                    #If RA is > 180 and < 0 or 360 then the motion will be to the right, otherwise to the left
                    #Or maybe if the number of required steps is < 0 then determine the motion
                '''
                
                ra_steps = float(compon[2])*num_of_stp_per_deg_ra #Number of RA steps from home position
                dec_steps = float(compon[4])*num_of_stp_per_deg_dec #Number of DEC steps from home position
                
                cur_stps = cfg_data.getSteps() #Get the current number of steps away from home position
                cur_stp_ra = cur_stps[0] #Get the current RA steps
                cur_stp_dec = cur_stps[1] #Get the current DEC steps
                
                #If the current steps variable is already corrected for a possible offset of home position from the true south, 
                #then remove the _steps_from_zero
                mov_stps_ra = cur_stp_ra + ra_steps + _steps_from_zero #Number of steps to move the RA motor
                mov_stps_dec = cur_stp_dec + dec_steps + _steps_from_zero #Number of steps to move the DEC motor
                
                #Get the current position of the dish from the magnetometer to use it later, before moving on
                
                #According to the sign of the mov_stps number decide at what direction to move, with negative indicating leftward direction
                #Replace the 1 in the arguments with the wanted delay
                if mov_stps_ra < 0:
                    ra_thr = threading.Thread(name = 'hourangle', target = self.motor.stepping_bckwd, args = (0.005, -mov_stps_ra, True))
                else:
                    ra_thr = threading.Thread(name = 'hourangle', target = self.motor.stepping_bckwd, args = (0.005, mov_stps_ra, True))
                
                if mov_stps_dec < 0:
                    dec_thr = threading.Thread(name = 'declination', target = self.motor.stepping_bckwd, args = (0.005, -mov_stps_dec, False))
                else:
                    dec_thr = threading.Thread(name = 'declination', target = self.motor.stepping_bckwd, args = (0.005, mov_stps_dec, False))
                ra_thr.start() #Start the thread for driving
                dec_thr.start() #Start the thread for driving
                while(not getattr(ra_thr, "done", False) and not getattr(dec_thr, "done", False)): #Wait until both threads finish
                    continue
                #ra_thr.join() #Close the thread
                #dec_thr.join() #Close the thread
                
                response = "POSITION_SET" #Send the correct message as formated above
                
                #Use the magnetometer to determine the current position and if the dish moved correctly before sending any message
                #After checking the correctness of the position assign the correct message to the response variable
                
                #ra_thr.run = False #Stops the execution of the thread
                #dec_thr.run = False #Stops the execution of the thread
                
                print("Received TRNST")
                
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