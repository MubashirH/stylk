"""This is a doc string
    HTis program checks if a number is fibonacci number. If not, then it will print the closest Fibonacci number to the input number
"""

def get_input():
    inp=int(raw_input('Enter the number'))
    return inp

def chec_fib(n):
    a=0
    b=1
    c=a+b
    while c<=n:
        if c==n:
            print '%d is a fibonacci number'%n
            return c
        a=b
        b=c
        c=a+b
    else:
        print '%d is not a fibonacci number'%n
        l=c-a
        x=n-l           #these three lines will compare whis is the closest fibonnica number to the input number
        y=c-n
        print l,'-<',n,'>-',c
        if x>y:
            print c,'is the closest Fibonacii number to %d'%n
        else:
            print l,'is the closest Fibonacii number to %d'%n

#main

n=get_input()
chec_fib(n)


    
