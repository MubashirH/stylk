"""This is a doc string
    This program will take multiple inputs and finds
    -the number of words in the input
    -the number of vowel'a'.
"""

def get_input():
    final=[]
    words=0
    length=0
    while True:
        
        inp=raw_input('Enter the sentence')
        if inp=='':
            break
        else:
            sen=inp.split()
            words=len(sen)
            length+=words
            final.append(inp)
    return final, length
        
def num_word(final,length):
    print 'no of words',length
    search=raw_input('enter the vowel u want to count:')
    f=''.join(final)
    print f.count(search)   
#main
final,length=get_input()
num_word(final,length)


