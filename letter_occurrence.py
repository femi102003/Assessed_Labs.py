def letter_occurrence(input_string):
    """
    This function counts the number of times the letter 'a' or 'A' appears in a given string.

    Parameters:
    ----------
    input_string : str
        The string in which to count occurrences of 'a' and 'A'.

    Returns: sss
    -------
    int:
        The count of 'a' and 'A' in the input string.
    """
    count = 0
    for char in input_string:
        if char == 'a' or char == 'A':
            count += 1
    return count

# Example usage
input_string = "Apples and Bananas"
print("The number of 'a' or 'A' in the string is:", letter_occurrence(input_string))  # Expected output: The number of 'a' or 'A' in the string is: 4