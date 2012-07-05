#script to cycle through items and print the question and answers

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
    while p < nanswers:
        #label each answer with a number, add one to avoid starting numbering from zero
        q = p + 1
        anumber = str(q)
        print '%s:' % anumber,
        #get the text of the relevant answer
        print canswers[p].text
        p = p + 1
    i = i + 1




