"""This program reads a file
    returns list of all the lines
"""
import sys
def get_lines():
    """ Reads the contents of filename
        and returns the - File handle
        - List of all lines of the file
    """
    f_name = raw_input('Enter the name of file to copy:')
    f_h = open(f_name, 'r')
    lines = f_h.read()
    f_h.close()
    print lines
    return lines
def write_lines(w_file, lin):
    """ Writes the lines into the a file whose
        filename is given as argument
    """
    n_fl = open(w_file, 'a')
    n_fl.writelines(lin)
    n_fl.close()
def main():
    """This the main"""
    if len(sys.argv) < 2:
        print "no file name provided to argument to program"
        quit()
    w_file = sys.argv[1]
    lin = get_lines()
    write_lines(w_file, lin)
if __name__ == '__main__':
    main()
