import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

class Analysis:
    def load_data(db_name = "data/expenses.db"):
        connection = sqlite3.connect(db_name)
        df = pd.read_sql_query("SELECT * FROM expenses", connection)
        connection.close()
        return df
    
    def plot_exp_by_category(df):
        category_totals = df.groupby("category")["amount"].sum()
        category_totals.plot(kind = "bar", title = "Expenses by Category", xlabel="Category", ylabel="Total Amount")
        plt.show()