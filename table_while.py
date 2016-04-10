"""This is a doc string
    This is a program which prints the table of 17
"""
def get_input():
    inp=int(input("Tell me which table do u desire\n")) #float or any other data type can be used 
    return inp

def table(b):
    i=1
    while i<=10:
        j=b*i
        print("%d * %d =%d"%(b,i,j)) # different data must b mentioned properly for desired execution
        i+=1
        
#main starts from here
b=get_input()
table(b)
