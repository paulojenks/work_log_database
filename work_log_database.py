#!/usr/bin/env python3

from collections import OrderedDict

import os

from search import Search
from add_task import AddTask
from view import View


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu():
    """Menu for Work Log"""
    choice = None

    while choice != 'q':
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print("{}) {}".format(key, value.__doc__))
        choice = input("Action:  ").lower().strip()

        if choice in menu:
            menu[choice]()

    print("Good Bye!")


menu = OrderedDict([
    ('a', AddTask),
    ('v', View),
    ('s', Search)
])


if __name__ == '__main__':
    main_menu()
