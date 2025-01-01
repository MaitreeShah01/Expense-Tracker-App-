import sqlite3

class dbhandler:
    def __init__(self, db_name="data/expenses.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS expenses ( 
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                date TEXT,
                category TEXT,
                description TEXT,
                amount REAL,
                FOREIGN KEY (user_id) REFERANCES users(id))""")
        

        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT) """)
        
        self.connection.commit()

    def add_expenses(self, date, category, description, amount):
        query = "INSERT INTO expenses (date, category, description, amount) VALUES (?, ?, ?, ?)"
        self.cursor.execute(query, (date, category, description, amount))
        self.connection.commit()

    def fetch_expenses(self):
        query = "SELECT * FROM expenses"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def close(self):
        self.connection.close()