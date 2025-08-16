def find_missing_number(arr):
    """
    Find the missing number in the array of size n-1 containing numbers from 1 to n.

    Parameters:
        arr (list): List of distinct integers from range 1 to n, missing one number.

    Returns:
        int: The missing number.
    """
    n = len(arr) + 1  # Since one number is missing
    expected_sum = n * (n + 1) // 2  # Sum of first n natural numbers
    actual_sum = sum(arr)            # Sum of given array
    return expected_sum - actual_sum


# ------------------ Testing ------------------ #

test_cases = [
    [1, 2, 4, 5],        # Missing 3
    [2, 3, 4, 5],        # Missing 1
    [1, 2, 3, 4],        # Missing 5
    [1],                 # Missing 2
    list(range(1, 1000000))  # Missing 1000000 (edge large case)
]

for arr in test_cases:
    print(f"Input: {arr[:10]}{'...' if len(arr) > 10 else ''}")  # Show partial input for large case
    print("Missing number:", find_missing_number(arr))
    print()
