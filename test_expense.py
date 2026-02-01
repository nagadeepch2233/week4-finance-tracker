from finance_tracker.expense import Expense

def test_expense_creation():
    e = Expense("2026-02-01", 500, "Food", "Groceries")
    assert e.amount == 500
    assert e.category == "Food"
    assert e.description == "Groceries"
    print("Expense test passed!")

if __name__ == "__main__":
    test_expense_creation()
