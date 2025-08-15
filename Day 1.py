def dutch_flag_algo_sort(nums):
    """
    Sort an array of 0s, 1s, and 2s in-place using Dutch National Flag Algorithm.
    
    Parameters:
        nums (list): List containing only 0, 1, and 2.
    """
    # Three pointers:
    start = 0           # Pointer for 0s position
    current = 0         # Pointer for current element
    end = len(nums) - 1 # Pointer for 2s position

    # Iterate until current passes end
    while current <= end:
        if nums[current] == 0:
            # Swap current with start, move both pointers forward
            nums[start], nums[current] = nums[current], nums[start]
            start += 1
            current += 1
        elif nums[current] == 2:
            # Swap current with end, move end pointer backward
            nums[current], nums[end] = nums[end], nums[current]
            end -= 1
            # Do NOT move current forward here because swapped value might be 0 or 2
        else:
            # If it's 1, just move current forward
            current += 1


# ------------------ Testing the function ------------------ #
test_cases = [
    [0, 1, 2, 1, 0, 2, 1, 0],
    [2, 0, 1],
    [0, 0, 0, 0],               # Edge Case : Same Elements
    [1, 1, 1, 1],               # Edge Case : Same Elements
    [2, 2, 2, 2],               # Edge Case : Same Elements
    [0, 1, 1, 2],               # Edge Case : Sorted
    [],                         # Edge Case : Empty
]

for arr in test_cases:
    dutch_flag_algo_sort(arr)
    print(arr)
