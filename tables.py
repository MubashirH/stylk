"""This is a doc string
    This is a program which prints the table of 17
"""
def get_input():
    inp=int(input("Tell me which table do u desire\n")) #float or any other data type can be used 
    return inp

def table(user):
    for i in range(0,11):
        j=a*i
        print("%d*%d equals %d"%(a,i,j)) # different data must b mentioned properly for desired execution
        
#main starts from here
a=get_input()
table(a)
