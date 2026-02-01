from finance_tracker.expense import Expense
from finance_tracker.file_handler import save_expenses, load_expenses
import os

def test_save_load():
    expenses = [Expense("2025-02-01", 1500, "Rent")]
    save_expenses(expenses)
    loaded = load_expenses()
    assert len(loaded) == 1
    assert loaded[0].amount == 1500
    assert loaded[0].category == "Rent"
    print("File handler test passed!")

if __name__ == "__main__":
    test_save_load()
