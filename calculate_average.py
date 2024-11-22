def calculate_average(numbers):
    """
    This function calculates the average of a list of numbers without using built-in Python functions.

    Parameters:
    ----------
    numbers : list
        A list of numerical values (int or float).

    Returns:
    -------
    float:
        The average of the numbers in the list. If the list is empty, returns None.

    Example:
    --------
    calculate_average([10, 20, 30, 40, 50])  # Output: 30.0
    """
    
    if not numbers:
        return None

    total = 0
    count = 0
    for number in numbers:
        total += number
        count += 1

    average = total / count
    return average

# Example usage
numbers = [38, 77, 49, 81, 124]
print("The average is:", calculate_average(numbers))  # Expected output: The average is: 73.8
