def celsius_to_fahrenheit(celsius):
    """
    This function converts a temperature from Celsius to Fahrenheit.

    Parameters:
    ----------
    celsius : float
        A number representing the temperature in Celsius.

    Returns:
    -------
    float:
        The equivalent temperature in Fahrenheit.
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Example usage
celsius = 25
print("The temperature in Fahrenheit is:", celsius_to_fahrenheit(celsius))  # Expected output: The temperature in Fahrenheit is: 77.0
