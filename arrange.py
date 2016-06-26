"""program to list of random numbers in assending order"""
import random
def rinput():
    """takes a number and generates that no of random list of numbers"""
    num = int(raw_input('enter number'))
    ln = random.sample(range(300,325),num)
    return ln, num
def arrange(l, n):
    """Arranges highest number in the list
        at the end of the list"""
    i = 0;
    for i in range(0,n-1):
        if l[i]>l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
    ans = l
def main():
    """This is main"""
    l, n = rinput()
    arrange(l, n)
if __name__ == '__main__':
    main()
