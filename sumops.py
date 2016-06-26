"""This program will take a 5 digit number as input
    return the sum of those 5 digits in number"""
import sys
def dsum(nums):
    """Calculates the sum"""
    ans = int(nums[0])+int(nums[1])+int(nums[2])+int(nums[3])+int(nums[4])
def main():
    """the main"""
    nums = str(sys.argv[1])
    dsum(nums)
if __name__ == '__main__':
    main()
