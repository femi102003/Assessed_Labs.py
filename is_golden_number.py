def is_golden_number(n):
    """
    This function checks if a given positive integer less than 1000 is a golden number.

    Parameters:
    ----------
    n : int
        A positive integer less than 1000.

    Returns: sss
    -------
    bool:
        True if the number is a golden number, otherwise False.
    """
    if n >= 1000:
        return False

    for a in range(1, n):
        b = n - a
        if a * b % 1000 == 0:
            return True

    return False

# Example usage
print(is_golden_number(65))  # Expected output: True
print(is_golden_number(70))  # Expected output: True
print(is_golden_number(61))  # Expected output: False