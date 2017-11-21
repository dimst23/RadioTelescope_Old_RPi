import RPi.GPIO as GPIO
import time

_full_step = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0]]
_half_step = [[1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 0]]

class motor(object):
    def GPIO_Init(self):
        #Set the pin numbering mode
        GPIO.setmode(GPIO.BOARD)
        
        #Set the output pins
        GPIO.setup(7, GPIO.OUT)
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(12, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)
        
        GPIO.setup(15, GPIO.OUT)
        GPIO.setup(16, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)
        
        GPIO.output(7, 0)
        GPIO.output(11, 0)
        GPIO.output(12, 0)
        GPIO.output(13, 0)
        
        GPIO.output(15, 0)
        GPIO.output(16, 0)
        GPIO.output(18, 0)
        GPIO.output(22, 0)
    
    def setStep(self, c1, c2, c3, c4, RA_motor):
        if RA_motor: #If RA_motor is True, then we are talking about the RA motor
            GPIO.output(7, c1)
            GPIO.output(11, c2)
            GPIO.output(12, c3)
            GPIO.output(13, c4)
        else:
            GPIO.output(15, c1)
            GPIO.output(16, c2)
            GPIO.output(18, c3)
            GPIO.output(22, c4)
    
    def full_step_fwd(self, delay, RA_motor):
        setStep(1, 0, 0, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 0)
        time.sleep(delay)
        setStep(0, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 0, 0, 1)
        time.sleep(delay)
        #setStep(1, 0, 0, 0)
        #time.sleep(delay)
    
    def full_step_bckwd(self, delay, RA_motor):
        setStep(1, 0, 0, 0)
        time.sleep(delay)
        setStep(0, 0, 0, 1)
        time.sleep(delay)
        setStep(0, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 0)
        time.sleep(delay)
        #setStep(1, 0, 0, 0)
        #time.sleep(delay)
    
    def half_step_fwd(self, delay, RA_motor):
        setStep(1, 0, 0, 0)
        time.sleep(delay)
        setStep(1, 1, 0, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 0)
        time.sleep(delay)
        setStep(0, 1, 1, 0)
        time.sleep(delay)
        setStep(0, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 0, 1, 1)
        time.sleep(delay)
        setStep(0, 0, 0, 1)
        time.sleep(delay)
        setStep(1, 0, 0, 1)
        time.sleep(delay)
        setStep(1, 0, 0, 0)
        time.sleep(delay)
    
    def half_step_bckwd(self, delay, RA_motor):
        setStep(1, 0, 0, 0)
        time.sleep(delay)
        setStep(1, 0, 0, 1)
        time.sleep(delay)
        setStep(0, 0, 0, 1)
        time.sleep(delay)
        setStep(0, 0, 1, 1)
        time.sleep(delay)
        setStep(0, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 0)
        time.sleep(delay)
        setStep(1, 1, 0, 0)
        time.sleep(delay)
        setStep(1, 0, 0, 0)
        time.sleep(delay)
    
    def RA_left(self, steps):
        
    
    
    def RA_right(self, steps):
        
    
    
    def DEC_up(self, steps):
        
    
    
    def DEC_down(self, steps):
        
    