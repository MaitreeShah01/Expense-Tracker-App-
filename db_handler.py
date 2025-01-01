import sqlite3
import bcrypt

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
                FOREIGN KEY (user_id) REFERENCES users(id))""")
        

        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT) """)
        
        self.connection.commit()

    def hash_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def verify_password(self, password, hashed_password):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

    def register_user(self, username, password):
        try:
            hashed_password = self.hash_password(password)
            self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            self.connection.commit()
            return "Registration successful."
        except sqlite3.IntegrityError:
            return "Username already exists."

    def login_user(self, username, password):
        self.cursor.execute("SELECT id, password FROM users WHERE username = ?", (username,))
        user = self.cursor.fetchone()
        if user and self.verify_password(password, user[1]):
            return user[0]  # Return user ID
        return None

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