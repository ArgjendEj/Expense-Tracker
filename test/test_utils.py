import sys
import os
import pytest

# Shto rrugën e projektit që Python ta gjejë utils.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import format_currency, validate_amount

def test_format_currency():
    assert format_currency(5) == "5.00 €"

def test_validate_amount_valid():
    assert validate_amount(10.5) is True

def test_validate_amount_invalid():
    assert validate_amount(-2) is False
    assert validate_amount("a") is False