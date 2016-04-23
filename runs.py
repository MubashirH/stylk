"""This is a doc string
    This program will take input of runs per ball, then do the following
    -total runs scored by the batsman
    -strike rate of batsman
    -no balls wasted
    -no of boundaries and sixes
"""
def get_input():
    """get the runs per ball"""
    print "enter runs per ball"
    bats_name = raw_input('Enter the batsman name:')
    i = int(raw_input('Enter no of balls faced by the batsman:'))
    n_ball = 1
    total_runs = []
    for n_ball in range(1, i+1):
        print n_ball, 'ball'
        run_s = raw_input('')
        if run_s is '':
            break
        elif run_s is '.':
            run_s = 0
            total_runs.append(run_s)
        else:
            ru_ns = int(run_s)
            total_runs.append(ru_ns)
        n_ball += 1
    return total_runs, bats_name, n_ball
def cal_runs(t_r, b_n, n_b):
    """calculates the desired output"""
    print 'Total runs scored by', b_n, sum(t_r)
    print 'Strike rate of', b_n, (sum(t_r)/n_b)
    print 'wasted balls', t_r.count(0)
    print 'boundaries', t_r.count(4)
    print 'sixes', t_r.count(6)
if __name__ == '__main__':
    t_r, b_n, n_b = get_input()
    cal_runs(t_r, b_n, n_b)
