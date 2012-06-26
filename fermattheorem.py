#script to take inputs for a, b, c, and n, and check that fermat's theorem holds
#i.e. check that a^n + b^n != c^n


#define the group of variables as a dictionary, and print the dictionary at the beginning
collection = {'a': 0, 'b': 0, 'c': 0, 'n': 0}
print collection 


#function to check whether variable contains an integer or a string
def check_integer(input):
    try:
        int(input)
    except ValueError:
        return 0

#loop through the elements of the dictionary asking for inputs
def get_numbers():
    for i in collection:
        collection[i] = raw_input('Please input number')
        print collection[i]
        #run check_integer function - for as long as it returns zero, keep asking to input number
        while check_integer(collection[i]) == 0:
            collection[i] = raw_input('try again!')
        collection[i] = int(collection[i])

#function to calculate left hand side
def lhs(a, b, n):
    lhs = a**n + b**n
    print 'the left hand side is %d' % lhs
    return lhs

#function to calculate right hand side
def rhs(c, n):
    rhs = c**n
    print 'the right hand side is %d' %rhs
    return rhs

#function to check whether two numbers are the same
def check_identity(left, right):
    if left == right:
        print 'the left and right are identical!'
    else:
        print 'fermat\'s theorem holds!'

#let's run this!

get_numbers()
l = lhs(collection['a'], collection['b'], collection['n'])
r = rhs(collection['c'], collection['n'])
check_identity(l, r)
print collection 

