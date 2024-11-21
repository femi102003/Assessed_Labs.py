def net_annual_income(gross_salary):
    """
    This function calculates the annual net income based on a given gross salary and applicable tax rates.

    Parameters:
    ----------
    gross_salary : float
        The total annual gross salary before tax.

    Returns: 
    -------
    float:
        The net annual salary after tax has been deducted.
    """
    if gross_salary >= 45000:
        tax_rate = 0.50
    elif 30000 <= gross_salary < 45000:
        tax_rate = 0.30
    else:
        tax_rate = 0.15

    net_salary = gross_salary * (1 - tax_rate)
    return net_salary

# Example usage
gross_salary = 50000
print("The net annual income is:", net_annual_income(gross_salary))  # Expected output: The net annual income is: 25000.0



