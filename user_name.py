"""This is a doc string
    This program will take the user name and the surname. Then it will give the output on the proper formate and also write the user name in the upper case letters
"""

def get_input():
    first=str(raw_input('Enter ur first name'))
    last=str(raw_input('Enter ur last name'))
    return str(first), str(last)

def formated_output(first, last):
   print '-Name:', first.lower(), ',Surname:',  last.lower() 
    print '-', first.upper(), last.upper()
    print '-'*10, '-'*5
    print '-', first.capitalize(), ',', last.capitalize()
    

#main
first,last=get_input()
formated_output(first,last)
