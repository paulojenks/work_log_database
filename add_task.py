from models import Entry


class AddTask:
    """Add some tasks"""
    def __init__(self):
        self.get_input()

    def get_input(self):
        """Add an entry to the work log"""
        print("What did you do?")
        name = input("Employee Name:\n>")
        task = input("What's the name of the task?\n>").lower()
        while True:
            try:
                minutes = int(input("How long did it take? (in minutes)\n>"))
                break
            except ValueError:
                print("Re-enter task length as integer")
        notes = input("Task Notes\n>").lower()
        save = input("Save Entry? [Yn]\n>").lower()

        if save != 'n':
            self.add_entry(name, task, minutes, notes)
            print("Saved Successfully")

    def add_entry(self, name, task, minutes, notes):
        Entry.create(name=name, task=task, minutes=minutes, notes=notes)
