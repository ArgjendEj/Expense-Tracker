import sqlite3
from datetime import datetime

DB_PATH = "data/expenses.db"

def get_connection():
    """Kthen një lidhje të re me bazën e të dhënave."""
    return sqlite3.connect(DB_PATH)

def init_db():
    """Krijon tabelën e shpenzimeve nëse nuk ekziston."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL
        )
        '''
    )

    conn.commit()
    conn.close()

def add_expense(description, amount):
    """Shton një shpenzim me validime."""
    if not description or not isinstance(amount, (int, float)) or amount <= 0:
        raise ValueError("Invalid expense data")

    conn = get_connection()
    cursor = conn.cursor()

    date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute(
        "INSERT INTO expenses (description, amount, date) VALUES (?, ?, ?)",
        (description, amount, date)
    )

    conn.commit()
    conn.close()

def get_all_expenses():
    """Kthen të gjitha shpenzimet si listë tuples."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    conn.close()
    return rows

def delete_expense(expense_id):
    """Fshin një shpenzim sipas ID-së."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))

    conn.commit()
    conn.close()
