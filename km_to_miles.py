def km_to_miles(kilometers):
    """
    This function converts a distance from kilometers to miles.

    Parameters:
    ----------
    kilometers : float
        A positive number representing the distance in kilometers.

    Returns:
    -------
    float:
        The equivalent distance in miles.
    """
    if kilometers < 0:
        return None  # or raise an exception if negative values are not allowed

    miles = kilometers * 0.621371
    return miles

# Example usage
kilometers = 10
print("The distance in miles is:", km_to_miles(kilometers))  # Expected output: The distance in miles is: 6.21371
