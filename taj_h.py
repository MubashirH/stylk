"""Program to calculate the following
    -Height of the Taj tower
    -Distance from the Taj gate to the gateway of india
    Angle of elivations are taken as input
"""
import math
def get_input():
    """take the elivations from different view points"""
    ang_gt = float(raw_input('Elivation angle from gateway of india to top of taj tower:'))
    ang_taj = float(raw_input('Elivation angle from Taj gate to top of taj tower:'))
    return ang_gt, ang_taj
def calculation(ang_g_t, ang_ta_j):
    """Algorithm to calculate the height n distance"""
    h_of_twr = round(math.tan(math.radians(ang_ta_j)) * 100)
    dis_to_gat = round((h_of_twr / math.tan(math.radians(ang_g_t))) - 100)
    print h_of_twr, 'yards is the height of the tower'
    print dis_to_gat, 'yards is the distace from Taj gate to the Gateway of India'
def main():
    """this is main"""
    ang_g_t, ang_ta_j = get_input()
    calculation(ang_g_t, ang_ta_j)
if __name__ == '__main__':
    main()
