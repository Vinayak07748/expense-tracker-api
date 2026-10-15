from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Expense Tracker API!"}

@app.get("/expenses")
def get_expenses():
    # Placeholder for fetching expenses from a database or other data source
    expenses = [
        {"id": 1, "description": "Groceries", "amount": 50.0},
        {"id": 2, "description": "Utilities", "amount": 100.0},
        {"id": 3, "description": "Rent", "amount": 1200.0}
    ]
    return {"expenses": expenses}

@app.get('/total-expenses')
def get_total():
    total = 50.0 + 100.0 + 1200.0  # Placeholder for calculating total expenses
    return {"total_expenses": total}
