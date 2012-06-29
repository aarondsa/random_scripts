#script to encrypt and decrypt text based on a user-inputted key

#global variables
#option decides whether the encrypt or decrypt functions are used
#1 is encrypt, 2 is decrypt
import sys
option = 0
text = 'empty'
key = 1



#function to encrypt text

def encrypt(text, key):
    print ('Welcome to the encryption function')
    letter_list = []
    code_list = []
    final_list = []
    for letter in text:
        letter_list.append(letter)
    for i in letter_list:
        code_list.append(ord(i))
    print code_list
    for i in code_list:
        final_list.append(key * int(i))     
    print final_list
        

#function to decrypt text

def decrypt(text, key):
    print ('Welcome to the decryption function')
    final_list = []
    code_list = []
    letter_list = []
    word_list = []
    final_list = (text.split(', '))
    print final_list
    for i in final_list:
        code_list.append(int(i))
    print code_list
    for i in code_list:
        letter_list.append(i / key)
    print letter_list
    for i in letter_list:
        word_list.append(chr(i))
    print word_list
    for i in word_list:
        sys.stdout.write(i),
    print '\n'     

#function to get text string

def get_text():
    global text
    print ('Please enter the text you wish to encrypt/decrypt')
    text = raw_input()
    
#function to get encryption/decryption key

def get_key():
    global key
    print ('Please enter the key you wish to use for encryption / decryption')
    key = int(raw_input())

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


menu()
get_text()
get_key()
select_function(option)

