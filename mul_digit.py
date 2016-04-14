"""This is a doc string
    This program will take a number as input and then print the following output
    -if one digit no then add 7 to it and print the unit digit no
    -if two digit no then do its power to 5 and print the last two digits
    -if 3 digit no then take another input of 3 digit no then add both of them
"""

def get_input():
    print 'Please enter a number up to 3 digits'
    num=int(raw_input('Enter a number'))
    while num>999:                              #this control flow statment will loop till a proper input is given i.e number up to 3 digits only
        print '!!wrong input!!, try again'
        num=int(raw_input('Enter a number'))
        continue
    return num

def calculation(num):
    if num<10:
        sum=num+7
        s=str(sum)          #converts the integer into a string
        print s[-1]
    elif 9<num<100:
        pro=num**5
        p=str(pro)          # converts the integer into a string
        print p[-2:]
    elif 99<num<1000:
        num_2=int(raw_input('enter a 3 digit number'))
        sum=num+num_2
        s2=str(sum)         # converts the integer into a string
        print s2[-3:]
        
#main
num=get_input()
calculation(num)

