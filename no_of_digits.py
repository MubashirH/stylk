"""This is a doc string
    This program will take an input number and tell the number of digits in the given number
"""

def get_input():
    n=str(raw_input('Enter the number:'))
    return n

def total(n):
    x=len(n)
    print x

#main
n=get_input()
total(n)
