from expense_manager import Exp_Manager
from analysis import Analysis

def main():
    manager = Exp_Manager()

    while True:
        print("\n --- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Expense Analysis")
        print("4. Export Expenses to CSV ")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_exp()
        elif choice == "2":
            manager.view_exp()
        elif choice == "3":
            df = Analysis.load_data()
            Analysis.plot_exp_by_category(df)
        elif choice == "4":
            manager.export_to_csv()
        elif choice == "5":
            manager.close()
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()