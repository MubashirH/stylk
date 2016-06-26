"""program to create a log table of base 10
    from  to 10
    from 1 to 100 in multiples of 10
"""
import math
def log():
    """Algorithm for finding the log base 10 of any number"""
    print ' Table 1'
    i = 1
    for i in range(1, 11):
        print i, '-- %.4f' %math.log(i, 10)
    print
    print ' Table 2'
    j = 10
    for j in range(10, 101, 10):
        print j, '-- %.4f' %math.log(j, 10)
    print 'Finish'
def main():
    """The main"""
    log()
if __name__ == '__main__':
    main()
