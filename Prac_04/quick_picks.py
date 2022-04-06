"""
CP1404/CP5632 Practical - Suggested Solution
Quick pick program
"""

import random

PER_LINE = 6
MIN = 1
MAX = 45


def main():
    no_of_picks = int(input("number of picks?  "))
    while no_of_picks < 0:
        print("invalid")
        no_of_picks = int(input("number of picks? "))

    for i in range(no_of_picks):
        quick_pick = []
        for j in range(PER_LINE):
            number = random.randint(MIN, MAX)
            while number in quick_pick:
                number = random.randint(MIN, MAX)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
