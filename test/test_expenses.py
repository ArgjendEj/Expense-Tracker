import sys
import os
import pytest

# Shto rrugën e projektit që Python ta gjejë expenses.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from expense import add_expense, get_all_expenses, delete_expense, init_db

def setup_function():
    """Ky funksion ekzekutohet para çdo testi për të pastruar bazën e të dhënave."""
    init_db()
    # Pastron të dhënat ekzistuese për testet
    expenses = get_all_expenses()
    for exp in expenses:
        delete_expense(exp[0])

def test_add_expense():
    add_expense("Kafe", 2.5)
    expenses = get_all_expenses()
    assert len(expenses) == 1
    assert expenses[0][1] == "Kafe"

def test_add_multiple_expenses():
    add_expense("Ushqim", 10.0)
    add_expense("Transport", 3.5)
    expenses = get_all_expenses()
    assert len(expenses) == 2

def test_delete_expense():
    add_expense("Buke", 1.2)
    expenses = get_all_expenses()
    exp_id = expenses[0][0]
    delete_expense(exp_id)
    expenses_after = get_all_expenses()
    assert len(expenses_after) == 0

def test_add_invalid_expense():
    with pytest.raises(ValueError):
        add_expense("", -5)

def test_database_initialization():
    init_db()
    expenses = get_all_expenses()
    assert isinstance(expenses, list)

