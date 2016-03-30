"""This is a doc string
   This program calculating the mileage of a vehicle
"""
def get_odo_input():
    start=float(input("Enter the start reading of odometer\n"))
    end=float(input("Enter the end reading of odometer\n")) #the following k and l will take the inputs from the user
    liters=float(input("Enter the amount of gas in liters\n"))
    return float(start), float(end), float(liters)

def cal_mileage(user):
    print("The mileage of your vehicle is=%f"%mileage)
      
# main starts from here
"""This is a doc string
    The complete calculation of the mileage is done in main
"""
start,end,liters=get_odo_input()
diff=end-start
mileage=diff/liters
cal_mileage(mileage)
    
