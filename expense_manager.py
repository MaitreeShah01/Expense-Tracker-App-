import sqlite3
import pandas as pd
from db_handler import dbhandler

class Exp_Manager:
    def __init__(self, user_id):
        self.user_id = user_id
        self.db = dbhandler()

    def add_exp(self):
        date = input("Enter date (YYYY-MM-DD) : ")
        category = input(" Enter category (e.g., Food, Rent, Travel): ")
        description = input("Enter description: ")
        amount = float(input("Enter amount: "))
        self.db.add_expenses(date, category, description, amount)
        print("Expense added successfully...!")

    def view_exp(self):
        expense = self.db.fetch_expenses()
        if not expense:
            print("No expenses found..")
        else:
            for exp in expense:
                print(f"{exp[0]} | {exp[1]} | {exp[2]} | {exp[3]} | {exp[4]:.2f} ")

    def export_to_csv(self, db_name = "data/expenses.db", csv_file="exports/expenses.csv"):
        try:
            connection = sqlite3.connect(db_name)

            df = pd.read_sql_query("SELECT * FROM expenses", connection)
            connection.close()

            df.to_csv(csv_file, index=False)
            print(f"Data exported successfully to {csv_file}")
        except Exception as e:
            print(f"Error exporting data: {e}")

    def close(self):
        self.db.close()