#script to write a table
# sys module is used for write function
import sys

#set the table parameters based on user input
col = int(raw_input("Enter the number of columns ")) 
row = int(raw_input("Enter the number of rows "))
col_width = int(raw_input("Enter the column width"))
row_height = int(raw_input("Enter the row height"))

#solidbar function creates a solid bar, alternating * and -
def solidbar (columns, col_width):
    sys.stdout.write('*'),
    p = 0
    while p < columns:
        sys.stdout.write("-" * col_width),
        sys.stdout.write("*")
        p = p + 1
    print ""

#broken bar function creates a single line of broken bars, with a | forming the columns, i.e. |   |   |   |   |   | 
def brokenbar (columns, col_width):
    sys.stdout.write('|')
    n = 0
    while n < columns:
        sys.stdout.write(" " * col_width),
        sys.stdout.write("|"),
        n = n + 1
    print ""

#brokenbarheight repeats the brokenbar function to create a row of varying height
def brokenbarheight (row_height):
    s = 0
    while s < row_height:
        brokenbar(col, col_width)
        s = s + 1

#this section writes the table
solidbar(col, col_width)
count = 0
while count < row:
    brokenbarheight(row_height)
    solidbar(col, col_width)
    count = count + 1
