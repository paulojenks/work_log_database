from collections import OrderedDict

from models import Entry
from view import View


class Search:
    """Search some previous Entries"""
    def __init__(self):
        self.get_search_input()

    def get_search_input(self):
        category = self.get_category()
        query = self.get_query(category)
        entries = self.search_params(category, query)
        View(entries)

    def get_category(self):
        """Get Search Category"""
        self.category = None

        while self.category is None:
            print("Enter 'q' to quit")
            for key, value in locations.items():
                print("{}) {}".format(key, value))
            self.category = input("Action: ").lower().strip()
            if self.category == "q":
                break
        return self.category

    def get_query(self, category):
        if self.category == "n":
            self.query = input("Enter employee's first and last name\n>")
        elif self.category == "k":
            self.query = input("Enter name of task\n>").lower().strip()
        elif self.category == "m":
            while True:
                try:
                    self.query = int(input("Enter duration(in minutes) of the task\n>"))
                    break
                except ValueError:
                    print("Try again!")
        else:
            self.query = input("Enter date (YYYY-MM-DD)\n>")

        return self.query

    def search_params(self, category, query):
        """Search Database using search parameters"""
        self.entries = Entry.select().order_by(Entry.timestamp.desc())

        if self.category:
            if self.category == "k":
                self.entries = self.entries.where(
                    (Entry.task.contains(query)) |
                    (Entry.notes.contains(query))
                )
            elif self.category == "m":
                self.entries = self.entries.where(Entry.minutes == query)
            elif self.category == "n":
                self.entries = self.entries.where(Entry.name.contains(query))
            else:
                self.entries = self.entries.where(Entry.timestamp == query)

        return self.entries


locations = OrderedDict([
    ("n", "Name"),
    ("k", "Keyword"),
    ("m", "Duration(Minutes)"),
    ("d", "Date")
])