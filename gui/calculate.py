#script to figure out how tkinter works

#this imports all the Tkinter stuff
from Tkinter import *

#create class for application
class stuff:

    def __init__(self, toplevel):
        
        self.frame = Frame(toplevel)
        self.frame.pack()
        
        #the command= argument says execute the function self.multiply when the button is clicked
        self.button = Button(self.frame, text='multiply', command=self.multiply)
        self.button.pack()

        #a repeat of the above button. now there are two buttons in the frame
        self.button = Button(self.frame, text='multiply', command=self.multiply)
        self.button.pack()
        

        #create a third button which does something in the frame, by calling function add_label
        #if the called function has closed brackets after it i.e. (), the function is called only once
        #and never again - i.e it is independent of button presses. i don't understand this...
        self.button = Button(self.frame, text='add label', command = self.add_label)
        self.button.pack()

        self.label = Label(self.frame, text='label')
        self.label.pack()

    #this function performs a simple multiplication and prints the result
    def multiply(self):
        a = 3
        b = 4
        result = a * b
        print result
    
    def add_label(self):
        self.label = Label(self.frame, text='new label!!!')
        self.label.pack()

#call tk() by assigning it to a variable. You have to call tk() at the beginning. 
root = Tk()
#call the application class. the argument is tk(), so that it is drawn in a window
app = stuff(root)
#keep running and waiting for user input
root.mainloop()
