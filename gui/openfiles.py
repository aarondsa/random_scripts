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
    print 'Word number %d is' % count
    #python counts from zero, so you need to subtract one from the number entered by the user
    count = count - 1
    print wordlist[count]
#    for debugging, this prints each consecutive item in wordlist
#    print 'the entire word list'
#    for i in wordlist:
#        print i

def longest_word():
    print 'Welcome to the longest word function'
    #two lists are required. the list of all the words, with a (length, word) tuple, and the list of the longest words 
    wordlist = []
    longlist = []
    #for each item in the file, create a tuple of (length, word) and put in wordlist
    for word in fileobject:
        wordlist.append(((len(word)), word))
    #sort wordlist, highest first
    wordlist.sort(reverse=True)
    #find the length of the longest word (a) and the longest word (b)
    a, b = wordlist[0]
    #remember that you need to subtract one from the length of each word
    print 'The length of the longest word(s) is %s' % (a - 1)
    #for each tuple in wordlist, if the length of the word equals the length of the longest word (a) add word to longlist
    for (x, y) in wordlist:
        if x == a:
            longlist.append(y)
    #for every item in longlist, print
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
