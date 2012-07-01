#script to encrypt and decrypt text based on a user-inputted key

#global variables
#option decides whether the encrypt or decrypt functions are used
#1 is encrypt, 2 is decrypt
import sys
option = 0
text = 'empty'
key = 1
a = 0
b = 0
c = 0

#function to encrypt text

        

#function to decrypt text

#function to get text string

def get_text():
    global text
    print ('Please enter the text you wish to encrypt/decrypt')
    text = raw_input()

#function to split the key into a, b, c

def split_key(key):
    global a, b, c
    keystr = str(key)
    a = int(keystr[0])
    b = int(keystr[:-1])
    c = int(keystr[-1])
    print a #defines the filler character
    print b # defines the multiplier
    print c #defines the character length

#function to multiply a number

def multiply(i, b):
    return (i*b)

#function to add suffix to produce string of defined character number

def fill(i, a, c):
    q = str(i)
    w = str(a)
    while len(q) < a:
        q = q + w
    return int(q)

#function to get encryption/decryption key
#the key is of the form xxxy, where there can be any number of x's, and the y dictates the character length
def get_key():
    global key
    print ('Please enter the key you wish to use for encryption / decryption')
    key = raw_input()

#function to analyse the key to check it is valid
#the criteria are longer than 3 digits, and last digit more than 3
def analyse_key(key):
    keystr = str(key)
    print 'len(keystr)'
    print len(keystr)
    print 'keystr[:-1]'
    print keystr[-1]
    if int(keystr[-1]) < 4:
        print 'The last digit needs to be greater than 3'
        return 2
    elif len(keystr) < 3:
        print 'The key needs to be at least 3 digits long'
        return 2
    else:
        return 1

#menu function to decide whether to encrypt or decrypt

def menu():
    global option
    option  = int(raw_input('Enter 1 for encryption and 2 for decryption'))

#select_function chooses between encryption and decryption

def select_function(option):
    if option == 1:
        print 'you chose encryption'
        encrypt(text, key)

    if option == 2:    
        print 'you chose decryption'
        decrypt(text, key)

get_text()
get_key()
while analyse_key(key) == 2:
    get_key()
split_key(key)

