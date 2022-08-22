# toto/lib.py
from termcolor import colored


def who_am_i():
    return colored('Hey my name is Roger', 'green')


if __name__ == '__main__':
    print(who_am_i)
