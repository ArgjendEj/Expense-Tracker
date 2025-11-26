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
        raise ValueError("Të dhëna të pavlefshme për shpenzimin.")

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
    if not isinstance(expense_id, int) or expense_id <= 0:
        raise ValueError("ID e pavlefshme për fshirje.")
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()

def update_expense(expense_id, new_description, new_amount):
    """Përditëson një shpenzim ekzistues (Feature 3)."""
    if not isinstance(expense_id, int) or expense_id <= 0:
        raise ValueError("ID e pavlefshme për update.")
    if not new_description or not isinstance(new_amount, (int, float)) or new_amount <= 0:
        raise ValueError("Të dhëna të pavlefshme për update.")

    conn = get_connection()
    cursor = conn.cursor()

    # Kontrollo nëse ekziston shpenzimi
    cursor.execute("SELECT id FROM expenses WHERE id = ?", (expense_id,))
    if cursor.fetchone() is None:
        conn.close()
        raise ValueError("Shpenzimi nuk ekziston.")

    # Përditëso të dhënat
    cursor.execute(
        "UPDATE expenses SET description = ?, amount = ? WHERE id = ?",
        (new_description, new_amount, expense_id)
    )
    conn.commit()
    conn.close()
