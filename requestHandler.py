import threading
#from motorDriver import motor
#import motorDriver

class requestHandle(object):
    #def __init__(self):
        #self.RAmotor = motor.RAmotor()
        #self.DECmotor = motor.DECmotor()
    
    def process(self, request):
        if request == "Test":
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
                print("Received TR")
            elif compon[0] == "AAF":
                #Handle the aim and follow function
                print("Received AAF")
        return response