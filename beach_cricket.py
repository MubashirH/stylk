"""This is a doc string
    This a program to monitor a beach cricket match
    -collects runs scored by each batsman
    -prints all the statistics of the complete game
"""
def get_input():
    """takes in multiple inputs"""
    name_1 = raw_input('name of 1st batsman:')
    name_2 = raw_input('name of 2nd batsman:')
    print 'write the name of batsman who is on strike and non-strike'
    strike = raw_input('strike')
    n_strike = raw_input('non-strike')
    return name_1, name_2, strike, n_strike
def beach_cal():
    """using the inputs calculates the desired output and prints it"""
    name_1, name_2, strike, n_strike = get_input()
    num = 1
    name_1_run = []
    name_2_run = []
    for num in range(1, 13):
        print num, 'ball'
        run = raw_input('')
        if run is '.':
            run = 0
        i_run = int(run)
        if name_1 is strike:
            name_1_run.append(i_run)
        elif name_2 is strike:
            name_2_run.append(i_run)
        if i_run % 2 is not 0:
            strike, n_strike = n_strike, strike
        if sum(name_1_run) is 60:
            break
        elif sum(name_2_run) is 60:
            break
        num += 1
        if num % 7 is 0:
            strike, n_strike = n_strike, strike
    print name_1_run, name_2_run
    print '*' * 10, name_1, '*' * 10
    print 'Total runs scored:', sum(name_1_run)
    print 'Strike rate:', float(sum(name_1_run) / num)
    print 'balls wasted', name_1_run.count(0)
    print 'boundaries', name_1_run.count(4)
    print 'sixes', name_1_run.count(6)
    print '*' * 10, name_2, '*' * 10
    print 'Total runs scored:', sum(name_2_run)
    print 'Strike rate:', float(sum(name_2_run) / num)
    print 'balls wasted', name_2_run.count(0)
    print 'boundaries', name_2_run.count(4)
    print 'sixes', name_2_run.count(6)    
#main
beach_cal()
