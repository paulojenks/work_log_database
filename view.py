from models import Entry


class View:
    """View some Entries"""
    def __init__(self, entries=None):
        if entries:
            entries = entries
        else:
            entries = Entry.select().order_by(Entry.timestamp.desc())
        self.view_entry(entries)

    def view_entry(self, entries):
        """View Entry"""
        for entry in entries:
            timestamp = entry.timestamp.strftime('%A %B %d')
            print(timestamp)
            print('=' * len(timestamp))
            print("Employee Name: {}".format(entry.name))
            print("Task: {}".format(entry.task))
            print("Duration: {}".format(entry.minutes))
            print("Notes: {}".format(entry.notes))
            print('=' * len(timestamp))
            print('n) next entry')
            print('d) delete entry')
            print('q) return main menu')

            next_action = input('Action: [Ndq] ').lower().strip()
            if next_action == 'q':
                break
            elif next_action == 'd':
                self.delete_entry(entry)

        if not entries:
            print("No Results")

    def delete_entry(self, entry):
        """Delete an entry"""
        if input("Are you sure?\n>").lower().strip() == 'y':
            entry.delete_instance()
            print("Entry Deleted")
