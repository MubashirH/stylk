"""This is a doc string
    This program takes an input from user then prints squares beginning from 1. All the square numbers should be less than the given input.
"""

def get_input():
    inp=int(raw_input('enter any number'))
    return int(inp)

def print_num_square(b):
    n=1
    m=n
    while m<b:
        m=n**2
        n+=1
        if m<b:
            print m

#main
b=get_input()
print_num_square(b)
    
