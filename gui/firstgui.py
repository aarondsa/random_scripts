#script to figure out how tkinter works

#this imports all the Tkinter stuff
from Tkinter import *

#create class for application
class stuff:

    #the __init__ function is automatically called whenever the class is called
    #all functions of a class must take the argument 'self'
    def __init__(self):
        print 'this is the init function!'
        a = raw_input()
        if a == '1':
            #to call a function of the same class, use self.nameoffunction(arg)
            #in this case the function is called 'function' - it takes no arguments
            self.function()

    #another function of the class 'stuff'
    #it is not the __init__ function, so is not called automatically
    #again it must take the argument self
    def function(self):    
        print 'welcome to the function!'

#call the class (automatically initiates the __init__ function of that class
app = stuff()

