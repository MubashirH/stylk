"""This is a doc string
    This program takes a string input. Then asks the user what part of the input string to replace with what
"""

def get_input():
    sen=str(raw_input('Enter the string:\n'))
    return sen

def replace(sen):
    print 'This is the entered string by you:--"',sen,'"'
    old=str(raw_input('Enter the word u wanna replace:'))
    new=str(raw_input('Enter the new word:'))
    print 'This is the new edited string:---','"',sen.replace(old,new,-1),'"'
    

#main
sen=get_input()
replace(sen)
