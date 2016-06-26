"""Program to calculate the following
    -Height of the Taj tower
    -Distance from the Taj gate to the gateway of india
    Given angle of elevation from
    Gateway of India = 25
    Taj hotel gate = 65
"""
import math
def calculation():
    """Algorithm to calculate the height n distance"""
    h_of_twr = round(math.tan(math.radians(65)) * 100)
    dis_to_gat = round((h_of_twr / math.tan(math.radians(25))) - 100)
    print h_of_twr, 'yards is the height of the tower'
    print dis_to_gat, 'yards is the distace from Taj gate to the Gateway of India'
def main():
    """this is main"""
    calculation()
if __name__ == '__main__':
    main()
