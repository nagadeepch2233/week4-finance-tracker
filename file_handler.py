import json, csv, os
from .expense import Expense

DATA_FILE = "data/expenses.json"
BACKUP_DIR = "data/backup"
EXPORT_DIR = "data/exports"

def save_expenses(expenses):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump([e.to_dict() for e in expenses], f, indent=4)

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE) as f:
        return [Expense.from_dict(d) for d in json.load(f)]

def backup_expenses():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    with open(os.path.join(BACKUP_DIR, "expenses_backup.json"), "w") as f:
        json.dump([e.to_dict() for e in load_expenses()], f, indent=4)

def export_to_csv(expenses, filename="expenses.csv"):
    os.makedirs(EXPORT_DIR, exist_ok=True)
    filepath = os.path.join(EXPORT_DIR, filename)
    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Amount", "Category", "Description"])
        for e in expenses:
            writer.writerow([e.date, e.amount, e.category, e.description])
