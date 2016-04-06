"""This is a Doc string
    This a program to monitor the levele of alchol in a factory
"""

def get_input():
    lvl=float(raw_input('Enter the current level of alcohol in liters'))
    cap=float(raw_input('Enter the total capacity'))
    return float(lvl), float(cap)

def level(lvl,cap):
    per=lvl/cap


    if per>.80:
        
        print'Danger !!!'
        print'Close the valve'
        
    elif per<.20:
        print'Time to re-fuel'

    else:    
        print'Hey!!\n Its okay, everything is undercontrol'

#main starts here
lvl,cap=get_input()
level(lvl,cap)
            
        
    
            
        
    
