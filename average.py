#!/usr/bin/env python3

# Created by Devin Jhu
# Created on May 2022
# The largest number finder


import random


def largest(number_array):
    # this function finds the largest number in the array

    largest_number = number_array[0]

    for counter in number_array:
        if counter > largest_number:
            largest_number = counter

    return largest_number


def main():
    # this function gets 10 random numbers 

    number_array = []

    print("The largest random number finder")

    # process
    for counter in range(0, 10):
        random_number = random.randint(0, 100)
        number_array.append(random_number)
        print("Random number: {}".format(random_number))

    largest_number = largest(number_array)

    # output
    print("The largest number is {0}.".format(largest_number))

    print("\nDone.")


if __name__ == "__main__":
    main()
