def find_maximum_difference(list1, list2):
    """
    This function finds the largest possible difference from two lists of numbers.

    Parameters:
    ----------
    list1 : list
        A non-empty 1-dimensional list of numbers.
    list2 : list
        A non-empty 1-dimensional list of numbers.

    Returns:
    -------
    int:
        The maximum difference between any elements from the first list and any element from the second list.
    """
    max_list1 = list1[0]
    min_list1 = list1[0]
    max_list2 = list2[0]
    min_list2 = list2[0]

    for num in list1:
        if num > max_list1:
            max_list1 = num
        if num < min_list1:
            min_list1 = num

    for num in list2:
        if num > max_list2:
            max_list2 = num
        if num < min_list2:
            min_list2 = num

    max_diff = max(abs(max_list1 - min_list2), abs(max_list2 - min_list1))
    return max_diff

# Example usage
print(find_maximum_difference([1, 5, 600], [100, 7, 3, 29, 39]))  # Expected output: 597
print(find_maximum_difference([1, 5, 600], [100, 7, 3, 602, 39]))  # Expected output: 601


