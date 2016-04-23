"""This is a doc string
    This program checks if a number is fibonacci number
    If not, then it will print the closest Fibonacci number to the input number
"""
def get_input():
    """get the input number"""
    inp = int(raw_input('Enter the number'))
    return inp

def chec_fib(n_n):
    """cal if the number is true or false"""
    a_a = 0
    b_b = 1
    c_c = a_a + b_b
    while c_c <= n_n:
        if c_c is n_n:
            print n_n, 'is a fibonacci number'
            return c_c
        a_a = b_b
        b_b = c_c
        c_c = a_a + b_b
    print n_n, 'is not a fibonacci number'
    d_diff = c_c - a_a
    x_x = n_n - d_diff
    y_y = c_c - n_n
    print d_diff, '-<', n_n, '>-', c_c
    if x_x > y_y:
        print c_c, 'is the closest Fibonacii number to', n_n
    else:
        print d_diff, 'is the closest Fibonacii number to', n_n
if __name__ == '__main__':
    n_n = get_input()
    chec_fib(n_n)
