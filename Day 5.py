def find_leaders(arr):
    n = len(arr)
    leaders = []
    max_from_right = float('-inf')  # initially very small

    # Traverse from right to left
    for i in range(n - 1, -1, -1):
        if arr[i] >= max_from_right:
            leaders.append(arr[i])   # arr[i] is a leader
            max_from_right = arr[i]  # update max
    
    # Reverse to maintain original order
    leaders.reverse()
    return leaders


# 🔹 Test Cases
test_cases = [
    [16, 17, 4, 3, 5, 2],        # Expected: [17, 5, 2]
    [1, 2, 3, 4, 0],             # Expected: [4, 0]
    [7, 10, 4, 10, 6, 5, 2],     # Expected: [10, 6, 5, 2]
    [5],                         # Expected: [5]
    [100, 50, 20, 10],           # Expected: [100, 50, 20, 10]
    list(range(1, 1000001))      # Expected: [1000000]
]

for arr in test_cases:
    result = find_leaders(arr)
    print(f"Input: {arr[:10]}{'...' if len(arr) > 10 else ''}")
    print("Leaders:", result[:10], "..." if len(result) > 10 else "")
    print()

