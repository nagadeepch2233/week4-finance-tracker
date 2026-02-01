from finance_tracker.expense import Expense
from finance_tracker.reports import monthly_summary, category_breakdown

def test_reports():
    expenses = [
        Expense("2025-02-01", 500, "Food"),
        Expense("2025-02-02", 1500, "Rent"),
        Expense("2025-02-03", 200, "Bus fare")
    ]
    print("Monthly Summary:")
    monthly_summary(expenses)
    print("\nCategory Breakdown:")
    category_breakdown(expenses)
    print("Reports test completed!")

if __name__ == "__main__":
    test_reports()
