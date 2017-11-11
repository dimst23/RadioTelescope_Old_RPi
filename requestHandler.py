import threading
#from motorDriver import RAmotor
#from motorDriver import DECmotor

class requestHandle(object):
    #def __init__(self):
        #self.RAmotor = RAmotor()
        #self.DECmotor = DECmotor()
    
    def process(self, request):
        if request == "Test":
            response = "OK"
        elif request == "Terminate":
            response = "Bye"
        else:
            compon = request.split("_")
            if compon[0] == "TRNST":
                #self.RAmotor
                #Handle the transit function
                break
            elif compon[0] == "AAF":
                #Handle the aim and follow function
                break
        return response