"""This is a doc string
    This a program to monitor a beach cricket match
    -collects runs scored by each batsman
    -prints all the statistics of the complete game
"""
def get_input():
    """takes in multiple inputs"""
    name_1 = raw_input('name of batsman on strike: ')
    name_2 = raw_input('name of batsman not on strike: ')
    strike = name_1
    n_strike = name_2
    print 'on strike: ', strike
    return name_1, name_2, strike, n_strike
def beach_cal(name_1, name_2, strike, n_strike):
    """using the inputs calculates the desired output and prints the output"""
    num = 1
    name_1_run = []
    name_2_run = []
    while num < 14:
        print num, 'ball'
        if sum(name_1_run) >= 15:
            print name_1, 'has scored', sum(name_1_run), 'runs, hence they won the game'
            break
        elif sum(name_2_run) >= 15:
            print name_2, 'has scored', sum(name_2_run), 'runs, hence they won the game'
            break
        run_1 = raw_input('')
        if run_1 == '':
            print strike, 'is out and his team has lost the game'
            break
        if run_1 == '.':
            run = 0
            if name_1 == strike:
                name_1_run.append(run)
            elif name_2 == strike:
                name_2_run.append(run)
            num += 1
            continue
        run_in = int(run_1)
        if run_in < 7:
            if name_1 == strike:
                name_1_run.append(run_in)
            elif name_2 == strike:
                name_2_run.append(run_in)
            if run_in % 2 != 0:
                strike, n_strike = n_strike, strike
            num += 1
            if (num-1) % 6 == 0:
                strike, n_strike = n_strike, strike
        else:
            print 'invalid input'
            print 'try again'
    print name_1_run, name_2_run
    return name_1_run, name_2_run
def stats(x_x, y_y):
    """this will print all the stats of individual players"""
    print '*' * 10, x_x, '*' * 10
    print 'Total runs scored:', sum(y_y)
    if sum(y_y) != 0:
        print 'Strike rate:', float(sum(y_y) / len(y_y))
    else:
        print 'strike rate: 0'
    print 'balls wasted', y_y.count(0)
    print 'boundaries', y_y.count(4)
    print 'sixes', y_y.count(6)
def main():
    """this is called as main function and will call all the functions"""
    name_1, name_2, strike, n_strike = get_input()
    name_1_run, name_2_run = beach_cal(name_1, name_2, strike, n_strike)
    stats(name_1, name_1_run)
    stats(name_2, name_2_run)
if __name__ == '__main__':
    main()
