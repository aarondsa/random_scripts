#script to put answers in a list, and in a dictionary
#the script then gets the correct answer from the file
#the script then calculates the number of the correct answer from the newly created dictionary
#the script then requests user input
#if the user input equals the number of the correct answer, the user can progress

from lxml import etree

#open and parse the file and set root
master = open('qfile.xml')
document = etree.parse(master)
print 'Document: %s' % document

root = document.getroot()


#find total number of items and set variable (nitems)
items = root.findall('item')
print items
nitems = len(items)
print nitems

#create citem object to cycle through
citem = root.xpath('item')
i = 0
while i < nitems:
    print '----------------------'
    print citem[i].text
    #cquestion = current question
    #get the current question. there is only ever one question per item, hence cquestion[0]
    cquestion = citem[i].xpath('question')
    print 'Question:',
    print cquestion[0].text

    #canswers = current answers
    #from the relevant item, get everything tagged answer and put it in canswers
    canswers = citem[i].xpath('answer')
    #find the number of answers (the length of canswers)
    nanswers = len(canswers)
    print 'Please choose one of the following %s options' % nanswers
    #loop through the answers printing them
    p = 0
    listanswers = []
    dictanswers = {} 
    while p < nanswers:
        #label each answer with a number, add one to avoid starting numbering from zero
        q = p + 1
        anumber = str(q)
        print '%s:' % anumber,
        #get the text of the relevant answer
        print canswers[p].text
        #this just adds a tuple to the list listanswers. the tuple consists of the answer number and the answer
        listanswers.append(((anumber), (canswers[p].text)))
        dictanswers[canswers[p].text] = anumber
        p =  p + 1
    #this just prints the tuple
    #note that the answers are printed three times in this script. once as separate print commands, and once as a tuple, and once from dictionary
    print listanswers
    print dictanswers
    #script to get the correct answer in trueans
    trueans = citem[i].xpath('true')
    print trueans[0].text
    #script to get the correct answer number from the dictionary dictanswers
    trueansnumber = dictanswers[trueans[0].text]
    print dictanswers[trueans[0].text]
    #script to get user input and store as userans
    userans = int(raw_input())
    if userans != int(trueansnumber):
        while userans != int(trueansnumber):
            print '%d is the wrong answer. Please try again' % userans
            userans = int(raw_input())
                    
    print 'Correct' 
    i = i + 1




