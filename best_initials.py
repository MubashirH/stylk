"""This is a doc string
    This program takes name of the user and finds the best possible intials by eliminating the last character
"""

def get_input():
    first=str(raw_input('Enter ur first name'))
    last=str(raw_input('Enter ur last name'))
    return str(first), str(last)

def best_initials(first,last):
    f=len(first)
    l=len(last)
    if l<f:
        n=f-l
        print first[:n+1],last[0]

    elif f<l:
        n=l-f
        print first[0],last[:n+1]
#main
first,last=get_input()
best_initials(first,last)
