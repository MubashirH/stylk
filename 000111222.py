"""this is a doc string
    This program takes input as number and does the following
    -if number is 5 output should be "00001111222233334444"
"""

def get_input():
    n=int(raw_input('Enter a number'))
    return n

def output(n):
    final=[]
    i=0
    while i<n:
        p=str(i)
        pro=p*(n-1)
        i+=1
        final.append(pro)
    print ''.join(final)

#main
n=get_input()
output(n)

