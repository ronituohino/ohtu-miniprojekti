import os
import sqlite3
import unittest
from database import Database
from repositories.book_reference_repo import BookReference


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database(testing_environment=True)
        # sqlite3.connect(os.path.join(dirname, "testi.db"))
        self.connection = self.db.get_database_connection()
        self.book_reference = BookReference

    def test_reset_database_creates_new_tables(self):
        self.db.reset_database()
        cursor = self.connection.cursor()

        data = cursor.execute(
            "SELECT id, author, title, year, publisher, bib_key FROM bookreferences").fetchall()
        self.assertEqual(data, [])

    def test_get_database_connection_returns_connection(self):
        self.assertNotEqual(self.db.get_database_connection, None)
