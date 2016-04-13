"""This is a doc string
    This program will take the user name and the surname. Then it will give the output on the proper formate and also write the user name in the upper case letters
"""

def get_input():
    first=str(raw_input('Enter ur first name'))
    last=str(raw_input('Enter ur last name'))
    return str(first), str(last)

def formated_output(first, last):
    print '-Name:', str.lower(first), ',Surname:',  str.lower(last) 
    print '-', str.upper(first), str.upper(last)
    print '-'*20, '-'*10
    print '-', str.capitalize(first), ',', str.capitalize(last)
    

#main
first,last=get_input()
formated_output(first,last)
