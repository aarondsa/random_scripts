#script to write a table

import sys

col = int(raw_input("Enter the number of columns ")) 
row = int(raw_input("Enter the number of rows "))
col_width = int(raw_input("Enter the column width"))
row_height = int(raw_input("Enter the row height"))

def solidbar (columns, col_width):
    sys.stdout.write('*'),
    p = 0
    while p < columns:
        sys.stdout.write("-" * col_width),
        sys.stdout.write("*")
        p = p + 1
    print ""

def brokenbar (columns, col_width):
    sys.stdout.write('|')
    n = 0
    while n < columns:
        sys.stdout.write(" " * col_width),
        sys.stdout.write("|"),
        n = n + 1
    print ""
    
def brokenbarheight (row_height):
    s = 0
    while s < row_height:
        brokenbar(col, col_width)
        s = s + 1
    
solidbar(col, col_width)
count = 0
while count < row:
    brokenbarheight(row_height)
    solidbar(col, col_width)
    count = count + 1
