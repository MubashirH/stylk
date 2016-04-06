"""This is a doc string
    this program is to take user input and output if its a 2 digit number or a 3 digit. If it neither then just print the number given by user
"""
def get_input():
    a=int(raw_input('Enter 1st number'))
    b=int(raw_input('Enter 2nd number'))
    return a, b

def num_comp(a,b):
    if 9<a<100:
        print a,'is a 2-digit number'
    elif 99<a<1000:
        print a,'is a 3-digit number'
    else:
        print a

    if 9<b<100:
        print b,'is a 2-digit number'
    elif 99<b<1000:
        print b,'is a 3-digit number'
    else:
        print b
              
    
#main
a,b=get_input()
num_comp(a,b)
