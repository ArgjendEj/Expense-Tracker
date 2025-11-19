import pytest
from expense import (
    add_expense,
    get_all_expenses,
    delete_expense,
    init_db
)

def test_add_expense():
    # Teston nëse shtimi i një shpenzimi funksionon
    add_expense("Kafe", 2.5)
    expenses = get_all_expenses()
    assert len(expenses) == 1
    assert expenses[0][1] == "Kafe"

def test_add_multiple_expenses():
    # Teston nëse mund të shtohen disa shpenzime
    add_expense("Ushqim", 10.0)
    add_expense("Transport", 3.5)
    expenses = get_all_expenses()
    assert len(expenses) == 2

def test_delete_expense():
    # Teston nëse fshirja e një shpenzimi punon
    add_expense("Buke", 1.2)
    expenses = get_all_expenses()
    exp_id = expenses[0][0]
    delete_expense(exp_id)
    expenses_after = get_all_expenses()
    assert len(expenses_after) == 0

def test_add_invalid_expense():
    # Teston nëse shtimi i një shpenzimi të pavlefshëm kthen gabim
    with pytest.raises(ValueError):
        add_expense("", -5)

def test_database_initialization():
    # Teston nëse inicializimi i bazës krijon tabelën
    init_db()
    expenses = get_all_expenses()
    assert isinstance(expenses, list)
