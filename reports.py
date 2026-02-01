from collections import defaultdict

def monthly_summary(expenses):
    total = sum(e.amount for e in expenses)
    print(f"Total Expenses: ₹{total:.2f}")

def category_breakdown(expenses):
    categories = defaultdict(float)
    for e in expenses:
        categories[e.category] += e.amount
    for cat, amt in categories.items():
        print(f"{cat}: ₹{amt:.2f}")

