"""Program for jacpot:-
    Takes 2 numbers adds them and compares with a random genarated number
    if same them win
"""
from sumops import dsum
import sys
import random
def get_input():
    """takes 2 numbers as input """
    while True:
        num = int(raw_input('Give me a 5 digit number:'))
        if 9999 < num < 100000:
            break
        else:
            print
            print '5 digit number only'
            continue
    return num
def jacpot(nu):
    """main algorithm to calculate the jacpot"""
    nu_n = str(nu)
    n_sum = dsum(nu_n)
    ran = random.randint(1,50)
    if n_sum == ran:
        print '!!!Congratualtions you have won the JACPOT!!!'
    else:
        print 'OOh Sorry you have lost'
        print 'The wining number is', ran
        print 'Better luck next time'
def main():
    l = sys.argv
    if (len(l)!= 1):
        nu = sys.argv[1]
        jacpot(nu)
    else:
        nu = get_input()
        jacpot(nu)
if __name__ == '__main__':
    main()

