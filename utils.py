def format_currency(amount):
    """Kthen shumën me simbol € dhe dy decimalë."""
    return f"{amount:.2f} €"

def validate_amount(amount):
    """Kontrollon nëse shuma është pozitive."""
    return isinstance(amount, (int, float)) and amount > 0
