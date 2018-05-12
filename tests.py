import unittest
from unittest.mock import patch

from work_log_database import *
from search import Search
from view import View

import models
from models import Entry


class MenuTests(unittest.TestCase):
    @patch('builtins.input')
    def test_main_menu(self, mock_input):
        mock_input.side_effect = ["q"]
        quit_menu = main_menu()
        self.assertIsNone(quit_menu)


class AddEntryTests(unittest.TestCase):
    def setUp(self):
        models.initialize()
        self.add_task_test = AddTask.__new__(AddTask)

    def tearDown(self):
        entry = Entry.get(Entry.select().where(Entry.task.contains("Test Task")))
        entry.delete_instance()
        models.db.close()

    @patch('builtins.input')
    def test_add_entry(self, mock):
        mock.side_effect = ["Test Name", "Test Task", 120, "Test Notes", "y", "q"]
        self.add_task_test.get_input()
        results = Entry.get(Entry.select().where(Entry.task.contains("Test Task")))
        self.assertIsNotNone(results)


class SearchTaskTests(unittest.TestCase):
    def setUp(self):
        models.initialize()
        self.search_test = Search.__new__(Search)

    def tearDown(self):
        models.db.close()

    @patch('builtins.input')
    def test_search(self, mock):
        mock.side_effect = ["n", "Test Name", "q"]
        try:
            self.search_test.get_search_input()
        except Entry.DoesNotExist:
            self.fail("Nope")


class ViewTasksTest(unittest.TestCase):
    def setUp(self):
        models.initialize()
        self.view_test = View.__new__(View)
        self.deletion_entry = Entry.create(name="Test Name", task="Test Task", minutes=120, notes="Test Notes")
        self.entries_test = Entry.get(Entry.select().where(Entry.task.contains("test task")))
        self.entry = self.entries_test


    def tearDown(self):
        entry = Entry.get(Entry.select().where(Entry.task.contains("Test Task")))
        entry.delete_instance()
        models.db.close()

    @patch('builtins.input')
    def test_delete_entry(self, mock):
        mock.side_effects = ["y"]
        self.view_test.delete_entry(self.entry)
        self.assertTrue(mock.called)


if __name__ == '__main__':
    unittest.main()
