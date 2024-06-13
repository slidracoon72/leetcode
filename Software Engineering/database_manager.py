import sqlite3


class DatabaseManager:
    """
    A singleton class to manage SQLite database operations for courses information.
    """
    _instance = None

    # Singleton strategy: Ensures only one instance of the class exists.
    def __new__(cls, *args, **kwargs):
        """
        Singleton pattern implementation to ensure only one instance of DatabaseManager exists.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            DatabaseManager: An instance of the DatabaseManager class.
        """
        if not cls._instance:
            cls._instance = super(DatabaseManager, cls).__new__(cls, *args, **kwargs)
            cls._instance.connection = sqlite3.connect('courses.db')

            # Database creation status message.
            if cls._instance.connection:
                print("Database 'courses.db' created!")
            else:
                print("Error creating a Database!")

            cls._instance.cursor = cls._instance.connection.cursor()
        return cls._instance

    def create_table(self):
        """
        Create 'courses' table in the database if it does not exist.

        Returns:
            None
        """
        # DRY: Create table query is defined separately.
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                semester TEXT,
                course TEXT,
                instructor TEXT,
                location TEXT
            )
        '''
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def insert_data(self, data):
        """
        Insert data into the 'courses' table.

        Args:
            data (list): List of tuples containing course information.

        Returns:
            None
        """
        # DRY: Insert query is defined separately.
        insert_query = '''
            INSERT INTO courses (semester, course, instructor, location)
            VALUES (?, ?, ?, ?)
        '''
        self.cursor.executemany(insert_query, data)
        self.connection.commit()

    def fetch_data(self):
        """
        Fetch all data from the 'courses' table.

        Returns:
            list: List of tuples containing fetched data.
        """
        # Fetch query for retrieving data from the database.
        fetch_query = 'SELECT * FROM courses'
        self.cursor.execute(fetch_query)

        return self.cursor.fetchall()
