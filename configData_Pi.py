import xml.etree.ElementTree as etree
import os

class confDataPi(object):
    #Class constructor
    def __init__(self, filename):
        self.filename = filename #Create a variable with the given filename
        self.parse() #Parse the XML file
    
    def parse(self):
        #Add a handling code for the case parsing fails
        self.tree = etree.parse(self.filename)
        self.root = self.tree.getroot()
        
    def getConfig(self, child, subchild):
        #self.parse()
        children = list(self.root.find(child))
        for item in children:
            if item.tag == subchild:
                return item.text
            else:
                continue
    
    def setConfig(self, element, child, value):
        elm = self.root.find(element) #Get the required element from the tree
        children = list(elm) #List the children of the element
        for item in children:
            if item.tag == child:
                item.text = value
                elm.set("updated", "yes")
                self.tree.write(self.filename)
                break
            else:
                continue
    
    def getSteps(self):
        return [float(self.getConfig("Steps", "RA")), float(self.getConfig("Steps", "DEC"))]
        
    def setSteps(self, m_steps):
        self.setConfig("Steps", "RA", float(m_steps[0]))
        self.setConfig("Steps", "DEC", float(m_steps[1]))
    
    def getPort(self):
        return self.getConfig("TCP", "port")
        
    def setPort(self, port):
        self.setConfig("TCP", "port", str(port))