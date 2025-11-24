def format_currency(amount: float) -> str:
    """Formaton një shumë numerike në tekst me dy decimalë dhe simbolin €.

    Args:
        amount (float): Shuma për t'u formatuar.

    Returns:
        str: Shuma e formatuar, p.sh. '5.00 €'.
    """
    try:
        return f"{float(amount):.2f} €"
    except (TypeError, ValueError):
        raise ValueError("Amount must be a numeric value")


def validate_amount(amount) -> bool:
    """Kontrollon nëse shuma është një numër i vlefshëm dhe më i madh se zero.

    Args:
        amount (any): Vlera e shumës.

    Returns:
        bool: True nëse shuma është numër dhe > 0, ndryshe False.
    """
    try:
        amount = float(amount)
        return amount > 0
    except (TypeError, ValueError):
        return False
