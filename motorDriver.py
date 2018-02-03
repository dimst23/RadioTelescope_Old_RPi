import RPi.GPIO as GPIO
import threading
import time

_steps = [[1, 0], [1, 1], [0, 1]]

class motor(object):
    def GPIO_Init(self):
        #Set the pin numbering mode
        GPIO.setmode(GPIO.BOARD)
        
        #Setup the output pins
        GPIO.setup(7, GPIO.OUT)
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(12, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)
        
        #Set the pins to LOW for the initial setup
        GPIO.output(7, 0)
        GPIO.output(11, 0)
        GPIO.output(12, 0)
        GPIO.output(13, 0)
    
    def setStep(self, c1, c2, RA_motor):
        if RA_motor: #If RA_motor is True, then we are talking about the RA motor
            GPIO.output(7, c1)
            GPIO.output(11, c2)
        else:
            GPIO.output(12, c3)
            GPIO.output(13, c4)
    
    def stepping_fwd(self, delay, steps, RA_motor):
        j = 0 #Initialize the indexing variable
        step = 0
        thr = threading.currentThread()
        while getattr(thr, "run", True) and (step < steps):
            self.setStep(_steps[j][0], _steps[j][1], RA_motor)
            time.sleep(delay)
            j = j + 1
            step = step + 1
            j = 0 if j == 3 else j
        thr.done = True #Indicate when we are done
    
    def stepping_bckwd(self, delay, steps, RA_motor):
        j = 0 #Initialize the indexing variable
        step = 0
        thr = threading.currentThread()
        while getattr(thr, "run", True) and (step < steps):
            self.setStep(_steps[3 - j][0], _steps[3 - j][1], RA_motor)
            time.sleep(delay)
            j = j + 1
            step = step + 1
            j = 0 if j == 3 else j
        thr.done = True #Indicate when we are done
    
    #def RA_left(self, steps):
        
    
    
    #def RA_right(self, steps):
        
    
    
    #def DEC_up(self, steps):
        
    
    
    #def DEC_down(self, steps):
        
    