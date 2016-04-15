"""This is a doc string
    This program takes name of the user and finds the best possible intials by eliminating the last character
"""

def get_input():
    first=str(raw_input('Enter ur first name'))
    last=str(raw_input('Enter ur last name'))
    return str(first), str(last)

def best_initials(first,last):
    n=-1
    print 'Options for ur initials'
    while len(first[:n])!=1 and len(last[:n])!=1:
        n-=1
        print first[:n], last[:n]
    else:
        print 'But this is the best solution of ur intitals'
        print first[:n], last[:n]
#main
first,last=get_input()
best_initials(first,last)
