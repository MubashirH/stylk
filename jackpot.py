"""Program for jacpot:-
    Takes 2 numbers adds them and compares with a random genarated number
    if same them win
"""
import sys
import random
from sumops import dsum
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
def jacpot(nu_n):
    """main algorithm to calculate the jacpot"""
    nu_nu = str(nu_n)
    n_sum = dsum(nu_nu)
    ran = random.randint(1, 50)
    if n_sum == ran:
        print '!!!Congratualtions you have won the JACPOT!!!'
    else:
        print 'OOh Sorry you have lost'
        print 'The wining number is', ran
        print 'Better luck next time'
def main():
    """The  main"""
    lgt = sys.argv
    if len(lgt) != 1:
        nu_n = sys.argv[1]
        jacpot(nu_n)
    else:
        nu_n = get_input()
        jacpot(nu_n)
if __name__ == '__main__':
    main()

