"""
    This program insert's some text in any given line of a file.
    Input :Filename is taken as argument to the program
            The user is prompted for the line where the text
            is to be inserted
    Output :The same file is updated with some new text
"""
import sys
def insert_text(wfh, lines, text, line_num):
    """
        Insert the text at a given line of a file
        Input :
                WFH : The file handle for the file opened in write mode
                all_lines : List of all lines in existing file
                new_text : A string of new text to be inserted in the file
                line_num : The line number where the file should be inserted
        Output :
                None
    """
    lines.insert(int(line_num-1), text)
    for line in lines:
        wfh.write(line)
        wfh.write('\n')
def get_linenumber(num):
    """
        Prompt the user for the line number where he wants to insert the text
        Input :
                The max number of lines in the existing file
        Output :
                A number that is less than the max number of lines in file
    """
    ans = num + 10 # Initialise ans to a number larger than number of lines
    while ans >= num:
        prompt = "Please enter the line number[max: " + str(num) + " ]"
        ans = raw_input(prompt)
        ans = int(ans)
    return ans
def print_file(f_h):
    """
        Print the contents of the file on the output screen
        Input :
                file handle
        Return :
                The number of lines in the file
                The list of all the lines in the existing file
    """
    all_text = f_h.read()
    all_lines = all_text.split('\n')
    for line in all_lines:
        print line
    return len(all_lines), all_lines
def main():
    """The main"""
    if len(sys.argv) < 2:
        print "No filename provided as argument to program"
        print "Usage :", sys.argv[0], "<filename>"
        quit()
    fname = sys.argv[1]
    text = raw_input('Write the line you want to insert:')
    f_h = open(fname)
    print "Printing the contents of file", fname
    (num_of_lines, lines) = print_file(f_h)
    f_h.close()
    line_number = get_linenumber(num_of_lines)
    wfh = open(fname, 'w')
    insert_text(wfh, lines, text, line_number)
    wfh.close()
    print "The use wants the text to be inserted in line number :", line_number
if __name__ == '__main__':
    main()
