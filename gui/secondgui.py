#script to figure out how tkinter works

#this imports all the Tkinter stuff
from Tkinter import *

#create class for application
class stuff:

    #__init__ takes a self argument, as all functions in a class do
    #it also takes another argument. This argument is the variable to which Tk() is assigned.
    #in this example the variable is called toplevel. it is supplied by 'root' below
    def __init__(self, toplevel):
        
        #create a frame. the argument is taken from the class: tk()
        #pack() actually draws the thing
        self.frame = Frame(toplevel)
        self.frame.pack()
        
        #create a button using x = Button(arguments)
        self.button = Button(self.frame, text='button')
        self.button.pack()
        
        #create a label using x = Label(arguments)
        self.label = Label(self.frame, text='label')
        self.label.pack()

#call tk() by assigning it to a variable. You have to call tk() at the beginning. 
root = Tk()
#call the application class. the argument is tk(), so that it is drawn in a window
app = stuff(root)
#keep running and waiting for user input
root.mainloop()
