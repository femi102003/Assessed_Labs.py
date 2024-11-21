def are_anagrams(str1, str2):
    """
    This function checks if two strings are anagrams of each other.

    Parameters:
    ----------
    str1 : str
        The first string to be compared.
    str2 : str
        The second string to be compared.

    Returns: sss
    -------
    bool:
        Returns True if the two strings are anagrams, otherwise False.

    Example:
    --------
    are_anagrams("listen", "silent")  # Output: True
    are_anagrams("hello", "world")    # Output: False
    """

    # Function implementation here ...
    # Anagrams have the same characters with the same frequency
    return sorted(str1) == sorted(str2)

## Example 
print(are_anagrams("listen", "silent"))  # Expected output: True
print(are_anagrams("hello", "world"))    # Expected output: False
