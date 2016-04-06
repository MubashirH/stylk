"""This is a doc string
    This program will calculate the percentage and grade the student
"""

def get_input():
    print 'Marks obtained'
    eng=float(raw_input('English'))
    sci=float(raw_input('Science'))
    math=float(raw_input('mathematics'))
    return float(eng), float(sci), float(math)

def cal_per(eng,sci,math):    
    a=(eng+sci+math)/270
    per=a*100
    print 'percentage obtained is  %f'%per

    if per<=35:
        print 'result is Fail'

    elif 35<per<75:
        print 'result is Average'
    
    elif 75<=per<90:
        print 'result is 2nd class'

    elif per>=90:
        print 'result is first class'
    
#main
eng,sci,math=get_input()
cal_per(eng,sci,math)

