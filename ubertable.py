#script to make table fillable with any value
import sys

#table parameters
ncolumns = int(raw_input("How many columns?"))
nrows = int(raw_input("How many rows?"))

#table contents
value = 0
def getvalue():
    global value
    value = int(raw_input("Enter a number between 0 and 9"))
    if value > 9:   
        getvalue()
    elif value < 0:
        getvalue()
    else:
        print "Thanks!" 

getvalue()
        
loc_column = int(raw_input("What column?"))
loc_row = int(raw_input("What row?"))


#draw table
#solidline function draws a solid line with as many columns as ncolumns
def solidline (col):
    sys.stdout.write("*"),
    col = 0
    while col < ncolumns: 
        sys.stdout.write("**") 
        col = col + 1
    print ""

#brokenline function draws a broken line, which has the value in the right spot
def brokenline (x):
    sys.stdout.write("|")
    x = 1
    while x <= ncolumns:
	if x == loc_column:
	    print value,
            sys.stdout.write("|")
            x = x + 1
        else:
            sys.stdout.write(" |")
            x = x + 1
    print ""

#brokenlineempty draws a broken line, with all of the boxes empty
def brokenlineempty (x):
    sys.stdout.write("|")
    x = 1
    while x <= ncolumns :
        sys.stdout.write(" |")
        x = x + 1
    print ""

#actually draw the table
solidline(ncolumns) #draw the solid line at the top
y = 1 #start counting rows
while y < nrows:
    if y == loc_row: 
        brokenline(ncolumns)
        y = y + 1
    else:
        brokenlineempty(ncolumns)
        y = y + 1
    solidline(ncolumns) #put a solid line beneath each row

