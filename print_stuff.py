"""This is a doc string
    This program will take an input as a sentence and print the following
    -last character
    -last 5 characters
    -2nd and 5th position characters
    -middle character with the two adjacent characters
"""


def get_input():
    sen=str(raw_input('Enter the desired sentence'))
    return str(sen)

def print_stuff(sen):
    print 'The last character is:', sen[-1]
    print 'the last 5 characters are:', sen[-5:]
    print '2nd position character is:', sen[1]
    if len(sen)>=5:
        print'5th position character is:',sen[4]
    else:
        print 'does not have a 5th element'
        
    l=len(sen)
    cen=l/2
    if l%2==0:
        print 'middle character with its adjacent characters:', sen[cen-2], sen[cen-1], sen[cen]
    else:
        print 'middle character with its adjacent characters:', sen[cen-1], sen[cen], sen[cen+1]
        
    

#main
sen=get_input()
print_stuff(sen)
