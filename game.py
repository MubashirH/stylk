"""program is a luck game simulating the following
    Asking 10 players to pick card btw 300-325
    The player with maximum number wins
"""
import random
from arrange import arrange
def get_input():
    """takes the names of the players"""
    players = int(raw_input('Enter no of players'))
    ply = players + 1
    names = []
    i = 0
    print
    print '----------Enter the names-----------'
    while i < ply-1:
        name = raw_input('Enter the name')
        while True:
            if name == '':
                print '----------Please enter a name-----------'
                name = raw_input('Enter the name')
            else:
                break
        names.append(name)
        i += 1
    return names, players
def game(nam, rng):
    """Algorithm of the game"""
    nums = random.sample(range(300, 325), rng)
    i = 0
    print
    print '----------These are the number cards-----------'
    while i < rng:
        print nam[i], '=', nums[i]
        i += 1
    grt = []
    for i  in range(rng):
        grt.append(nums[i])
    arrange(grt, rng)
    for i in range(rng):
        if nums[i] != grt[rng-1]:
            continue
        else:
            print
            print nam[i], 'has won the game'
            break
def main():
    """This is the main"""
    nam, rng = get_input()
    game(nam, rng)
if __name__ == '__main__':
    main()

