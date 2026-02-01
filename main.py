from .expense import Expense
from .expense_manager import ExpenseManager
from .file_handler import save_expenses, load_expenses, backup_expenses, export_to_csv
from .reports import monthly_summary, category_breakdown

class FinanceApp:
    def __init__(self):
        self.manager = ExpenseManager()
        self.manager.expenses = load_expenses()

    def run(self):
        print("===== FINANCE TRACKER =====")
        while True:
            print("\n1.Add 2.View 3.Search 4.Monthly Report 5.Category 6.Export 0.Exit")
            choice = input("Choice: ")
            if choice == "1":
                date = input("Date (YYYY-MM-DD): ")
                amount = float(input("Amount: "))
                category = input("Category: ")
                desc = input("Description: ")
                self.manager.add_expense(Expense(date, amount, category, desc))
                save_expenses(self.manager.expenses)
            elif choice == "2":
                for e in self.manager.expenses:
                    print(e.to_dict())
            elif choice == "3":
                key = input("Keyword: ")
                for e in self.manager.search_expenses(key):
                    print(e.to_dict())
            elif choice == "4":
                monthly_summary(self.manager.expenses)
            elif choice == "5":
                category_breakdown(self.manager.expenses)
            elif choice == "6":
                export_to_csv(self.manager.expenses)
            elif choice == "0":
                print("Exiting...")
                break
            else:
                print("Invalid choice!")
