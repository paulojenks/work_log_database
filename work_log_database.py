#!/usr/bin/env python3

from collections import OrderedDict
from models import clear_screen


from search import Search
from add_task import AddTask
from view import View


def main_menu():
    """Menu for Work Log"""
    choice = None

    while choice != 'q':
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print("{}) {}".format(key, value.__doc__))
        choice = input("Action:  ").lower().strip()
        clear_screen()

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
