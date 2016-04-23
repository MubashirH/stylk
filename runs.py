"""This is a doc string
    This program will take input of runs per ball, then do the following
    -total runs scored by the batsman
    -strike rate of batsman
    -no balls wasted
    -no of boundaries and sixes
"""

def get_input():
    print "enter runs per ball"
    name=raw_input('Enter the batsman name:')
    i=int(raw_input('Enter no of balls faced by the batsman:'))
    n=1
    runs=[]
    for n in range (1,i+1):
        print n,'ball'
        run=raw_input('')
        if run=='':
            break
        elif run=='.':
            run=0
            runs.append(run)
        else:
            ru=int(run)
            runs.append(ru)
        n+=1
    return runs, name, n

def cal_runs(r,ne,n):
    print 'Total runs scored by',ne,sum(r)
    print 'Strike rate of',ne,(sum(r)/n)
    print 'wasted balls',r.count(0)
    print 'boundaries',r.count(4)
    print 'sixes',r.count(6)
    
        

if __name_=='__main__':
    r,ne,n=get_input()
    cal_runs(r,ne,n)
