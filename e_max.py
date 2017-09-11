"""This program takes the input as file name in the argument line
   Finds the max occurance of the ltter "e"
"""
import sys
def get_lines():
    """ Reads the contents of filename
        and returns the - File handle
        - List of all lines of the file
    """
    f_name = raw_input('Enter the name of file:')
    try:
        FH = open(f_name, 'r')
    except(IOError):
        print "Check te file name and re-try"
        quit()
    lines = FH.read()
    FH.close()
    return lines

def write_lines(fil):
    """ Finds the maximun occurance of the number e"""
    print fil
    sep_1 = fil.splitlines()
    print sep_1
    print len(sep_1)
    i = 0
    num = []
    for i in range(len(sep_1)):
        sep_2 = list(sep_1[i])
        print sep_2
        num.append(sep_2.count("e"))
    print num
    print "Line number", num.index(max(num)), "has the max number of e's"


    
def main():
    """This the main"""
    if len(sys.argv) < 2:
        print "no file name provided as argument to program"
        print 
        lin = get_lines()
        write_lines(lin)
    else:
        w_file = sys.argv[1]
        try:
            FH = open(w_file, 'r')
        except(IOError):
             print "Check the file name and re-try"
             quit()
        lines = FH.read()
        write_lines(lines)
        FH.close()
    
if __name__ == '__main__':
    main()
    
