import sys
import os
import pytest

# Shto rrugën e projektit që Python ta gjejë expenses.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from expense import add_expense, get_all_expenses, delete_expense, init_db

def setup_function():
    """Ekzekutohet para çdo testi – garanton DB të pastër (TDD)."""
    init_db()
    # Pastrimi manual i të dhënave
    expenses = get_all_expenses()
    for exp in expenses:
        delete_expense(exp[0])

# -----------------------------
#     FEATURE 1 TESTS
# -----------------------------

def test_add_expense():
    """Teston shtimin e një shpenzimi (Feature 1)."""
    add_expense("Kafe", 2.5)
    expenses = get_all_expenses()
    assert len(expenses) == 1
    assert expenses[0][1] == "Kafe"

def test_add_multiple_expenses():
    """Teston shtimin e disa shpenzimeve njëkohësisht (Feature 1)."""
    add_expense("Ushqim", 10.0)
    add_expense("Transport", 3.5)
    expenses = get_all_expenses()
    assert len(expenses) == 2

def test_add_invalid_expense():
    """Teston sjelljen me të dhëna të pavlefshme (Feature 1 – Error Handling)."""
    with pytest.raises(ValueError):
        add_expense("", -5)

# -----------------------------
#     FEATURE 2 TESTS
# -----------------------------

def test_delete_expense():
    """Teston fshirjen e një shpenzimi (Feature 2)."""
    add_expense("Buke", 1.2)
    expenses = get_all_expenses()
    exp_id = expenses[0][0]  # merr ID
    delete_expense(exp_id)
    expenses_after = get_all_expenses()
    assert len(expenses_after) == 0

# -----------------------------
#     EXTRA VALIDATION
# -----------------------------

def test_database_initialization():
    """Kontrollon që DB kthehet si list (sanity check)."""
    init_db()
    expenses = get_all_expenses()
    assert isinstance(expenses, list)
