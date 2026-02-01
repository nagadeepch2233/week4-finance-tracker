from .expense import Expense

class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense: Expense):
        self.expenses.append(expense)

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]

    def search_expenses(self, keyword):
        return [e for e in self.expenses
                if keyword.lower() in e.category.lower() 
                or keyword.lower() in e.description.lower()]

    def filter_by_month(self, year, month):
        return [e for e in self.expenses if e.date.year == year and e.date.month == month]
