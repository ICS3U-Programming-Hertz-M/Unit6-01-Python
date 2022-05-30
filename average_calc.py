#!/usr/bin/env python3

# Created by: hertz
# Created on: May 30, 2022.
# This program generates 10 random numbers from 0 to 100 then
# displays the position number of the random number
# calculates the average and displays it to the user.


import constants
import random


def main():
    # initialize sum ,counter and create a list.
    counter = 0
    sum = 0
    list_int = []

    # Generate random number to the user.
    for counter in range(constants.MAX_SIZE):
        list_int.append(random.randint(constants.MIN_NUM, constants.MAX_NUM))
        sum = sum + list_int[counter]
        print("{} is added to the list at position {}"
              .format(list_int[counter], counter))

    # calculates the average and displays it to the user.
    for counter in range(1):
        avrg = sum / constants.MAX_SIZE
        print("")
        print("{} is the average.".format(avrg))


if __name__ == "__main__":
    main()
