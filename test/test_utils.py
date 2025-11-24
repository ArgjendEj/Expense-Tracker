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

# ===============================
# FEATURE 2 — TESTE TË REJA
# ===============================

def test_format_currency_large_number():
    """Teston formatimin e një vlere shumë të madhe."""
    assert format_currency(1234567.89) == "1234567.89 €"

def test_format_currency_with_float():
    """Teston formatim korrekt me shumë dhjetore."""
    assert format_currency(2.3456) == "2.35 €"

def test_validate_amount_zero():
    """0 nuk duhet të pranohet si vlerë valide."""
    assert validate_amount(0) is False

def test_validate_amount_none():
    """None nuk është vlerë valide."""
    assert validate_amount(None) is False

def test_validate_amount_empty_string():
    """String i zbrazët nuk duhet pranuar."""
    assert validate_amount("") is False