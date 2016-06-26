"""Program to calculate height of a solid 3cm radius cylinder
    made from a hollow sphere whose radii are given as input
    if input is not in "cm" then it will converted
"""
from math import pi
def get_input():
    """take the radii of hollow sphere"""
    radi_1 = float(raw_input('Enter outer radius:'))
    radi_2 = float(raw_input('Enter inner radius:'))
    radi_3 = float(raw_input('Enter radius of cylinder to be made:'))
    return radi_1, radi_2, radi_3
def cylinder(rad_1, rad_2, rad_3):
    """Algorithm to calculate the height of the designed cylinder"""
    v_of_out_sph = 4/3 * pi * rad_1 ** 3
    v_of_inr_sph = 4/3 * pi * rad_2 ** 3
    v_of_sph = v_of_out_sph - v_of_inr_sph
    v_of_cyl = v_of_sph - (v_of_sph * 0.05)
    h_of_cyl = v_of_cyl / (pi * rad_3 ** 2)
    print h_of_cyl, 'cm is the Height of the solid cylinder'
def main():
    """The main"""
    rad_1, rad_2, rad_3 = get_input()
    cylinder(rad_1, rad_2, rad_3)
if __name__ == '__main__':
    main()
