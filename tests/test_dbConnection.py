import unittest
from unittest.mock import MagicMock
from src.dbConnection import DbConnection


class MyTestCase(unittest.TestCase):
    def setUp(self):
        # Create a new instance of the DbConnection class
        self.db = DbConnection()

    def test_connect_to_db(self):
        # simulating proper connection
        mock_connection = MagicMock()
        # mock connection string

        with unittest.mock.patch('pyodbc.connect', return_value=mock_connection):
            conn = self.db.connect_to_db()
            self.assertEqual(conn, mock_connection)


if __name__ == '__main__':
    unittest.main()
