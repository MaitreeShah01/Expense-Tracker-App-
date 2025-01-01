from expense_manager import Exp_Manager
from analysis import Analysis
from db_handler import dbhandler

def main():
    db = dbhandler()
    user_id = None
    #manager = Exp_Manager()

    while not user_id:
        print("\n--- Authentication ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(db.register_user(username, password))
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_id = db.login_user(username, password)
            if user_id:
                print("Login successful!")
            else:
                print("Invalid username or password.")
        elif choice == "3":
            db.close()
            print("Exiting...")
            return
        else:
            print("Invalid choice. Please try again.")

    manager = Exp_Manager(user_id)
    
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
    
    db.close()

if __name__ == "__main__":
    main()