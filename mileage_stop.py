"""This is a doc string
   This program calculating the mileage of a vehicle
"""
def get_input():
    start=float(input("Enter the start reading of odometer\n"))
    end=float(input("Enter the end reading of odometer\n")) 
    cap=float(input("Enter the total fuel capacity of your vehical\n"))
    dist=int(input("enter the total distance to be travelled\n"))
    return float(start), float(end), float(cap), float(dist)

def cal_stops(user):
    print("no of re-fuel stops required = %f"%c)
      
# main starts from here
"""This is a doc string
    The complete calculation is done in main
"""
start,end,cap,dist=get_input()
diff=end-start
a=diff/cap
b=dist/a
c=b/cap
cal_stops(c)
    
