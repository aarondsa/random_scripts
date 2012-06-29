#script to play with opening text files
#still need to give the script a gui to make it fit in the gui folder...
fileobject = open('words')
print fileobject


#functions which can be applied to the word list
def all_words():
    print 'Welcome to the all words function'
    for word in fileobject:
        print word

def nth_word():
    print 'the nth word function'
    wordlist = []
    for word in fileobject:
        wordlist.append(word)

    count = int(raw_input('Which word number would you like?'))
    print 'your chosen word'
    print wordlist[count]
#    for debugging, this prints each consecutive item in wordlist
#    print 'the entire word list'
#    for i in wordlist:
#        print i

def longest_word():
    print 'Welcome to the longest word function'
    wordlist = []
    longlist = []
    for word in fileobject:
        wordlist.append(((len(word)), word))
    wordlist.sort(reverse=True)
    a, b = wordlist[0]
    print 'The length of the longest word(s) is %s' % a
    for (x, y) in wordlist:
        if x == a:
            longlist.append(y)
    for x  in longlist:
        print x

#print menu of functions
print 'Print all words  1\nPrint nth word  2\nPrint the longest word  3\n'

#choose function
def menu_function():
    print 'Please enter the number of the desired function'
    option = 4
    while option > 3:
        option = int(raw_input())
        if option == 1:
            all_words()
        if option == 2:
            nth_word()
        if option == 3:
            longest_word()
menu_function()
