from tkinter import Tk, Label, Entry, Button, Text, END
from expense_manager import Exp_Manager

def add_expense_gui():
    def save_expense():
        date = date_entry.get()
        category = category_entry.get()
        description = description_entry.get()
        amount = amount_entry.get()
        manager.db.add_expenses(date, category, description, float(amount))
        status_label.config(text="Expense added successfully!")
        date_entry.delete(0, END)
        category_entry.delete(0, END)
        description_entry.delete(0, END)
        amount_entry.delete(0, END)

    root = Tk()
    root.title("Expense Tracker")

    Label(root, text="Date (YYYY-MM-DD):").grid(row=0, column=0)
    date_entry = Entry(root)
    date_entry.grid(row=0, column=1)

    Label(root, text="Category:").grid(row=1, column=0)
    category_entry = Entry(root)
    category_entry.grid(row=1, column=1)

    Label(root, text="Description:").grid(row=2, column=0)
    description_entry = Entry(root)
    description_entry.grid(row=2, column=1)

    Label(root, text="Amount:").grid(row=3, column=0)
    amount_entry = Entry(root)
    amount_entry.grid(row=3, column=1)

    Button(root, text="Add Expense", command=save_expense).grid(row=4, column=1)
    status_label = Label(root, text="")
    status_label.grid(row=5, column=1)

    root.mainloop()

manager = Exp_Manager()
add_expense_gui()
