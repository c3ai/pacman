"""
Board generator for FDS PACMAN hiring test
Date Modified: Apr 16, 2018

How to run:
Run in command-line, specifying the output text file name as follows:

Python2:
$ python board_generator.py textfilename.txt

Python3:
$ python3 board_generator.py textfilename.txt
"""

import sys
import random

# tunable parameters
board_dimension = 3000
total_movements = 400
total_walls = 600

# don't touch
possible_movements = ["N", "E", "S", "W"]


def generate(file_name):
    # generate list of movements
    movement_list = "".join(
        [possible_movements[random.randint(0, 3)] for i in range(total_movements)])

    # generate list of walls
    wall_list = set([(random.randint(1, board_dimension-1),
                      random.randint(1, board_dimension-1)) for k in range(total_walls)])

    # generate initial position and make sure it is not on a wall
    while(len(wall_list) > 0):
        initial_position = random.randint(
            1, board_dimension-1), random.randint(1, board_dimension-1)
        if initial_position not in wall_list:
            break

    # write text file
    f = open(file_name, "w+")
    f.write(" ".join([str(board_dimension), str(board_dimension)])+"\n")
    f.write(" ".join([str(initial_position[0]),
                      str(initial_position[1])])+"\n")
    f.write(movement_list + "\n")
    for item in wall_list:
        f.write(" ".join([str(item[0]), str(item[0])])+"\n")
    return


if __name__ == '__main__':
    generate(sys.argv[1])
