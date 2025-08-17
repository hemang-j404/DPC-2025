def find_duplicate_number(arr):
    """
    Find the duplicate number in an array using Floyd's Cycle Detection Algorithm.
    
    Parameters:
        arr (list): List of n+1 integers where each is in range [1, n].
    
    Returns:
        int: The duplicate number.
    """

    # ------------------ Phase 1: Detect cycle ------------------
    tortoise = arr[0]
    hare = arr[0]

    while True:
        tortoise = arr[tortoise]        # Move tortoise 1 step
        hare = arr[arr[hare]]           # Move hare 2 steps
        if tortoise == hare:
            break                       # Cycle detected

    # ------------------ Phase 2: Find cycle entry ------------------
    tortoise = arr[0]                   # Reset tortoise to start
    while tortoise != hare:
        tortoise = arr[tortoise]        # Move 1 step
        hare = arr[hare]                # Move 1 step
    
    return hare   # Both meet at duplicate number


# ------------------ Testing the function ------------------ #

test_cases = [
    [1, 3, 4, 2, 2],                 # Duplicate: 2
    [3, 1, 3, 4, 2],                 # Duplicate: 3
    [1, 1],                          # Duplicate: 1 (edge case smallest n)
    [1, 4, 4, 2, 3],                 # Duplicate: 4
    [2, 5, 9, 6, 9, 3, 8, 9, 7, 1], # Duplicate: 9 (duplicate appears more than twice)
    list(range(1, 100000)) + [50000] # Duplicate: 50000 (large edge case)
]

for arr in test_cases:
    print(f"Input: {arr[:10]}{'...' if len(arr) > 10 else ''}")  # show first 10 elements for large input
    print("Duplicate number:", find_duplicate_number(arr))
    print()
