"""this is a doc string
    A program to take input from the user and produce it back
"""
def get_input():
    inp=input("what is ur name\n")
    return inp
def say_hello(user):
    print("hello",name,"!!!")

#main starts from here
"""this is a doc string
    this to call the functions declared above
"""
name=get_input()
say_hello(name)
