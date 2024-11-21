def fuel_cost(distance_miles):
    """
    This function calculates the total fuel cost given a travelled distance in miles.

    Parameters:
    ----------
    distance_miles : float
        The travelled journey in miles (positive number).

    Returns:
    -------
    float:
        The total cost of fuel in pounds (£) for the given distance.
    """
    # Constants
    MPG = 50  # Miles per gallon
    LITERS_PER_GALLON = 4.5
    PRICE_PER_LITER = 1.49  # Price in pounds per liter

    # Calculate total fuel cost
    total_cost = PRICE_PER_LITER * (distance_miles / MPG) * LITERS_PER_GALLON
    return total_cost

# Example usage
distance_miles = 50
print("The total fuel cost is: £", fuel_cost(distance_miles))  # Expected output: The total fuel cost is: £6.705
