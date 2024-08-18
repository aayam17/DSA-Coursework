def longest_hike(trail, k):
    if not trail:
        return 0

    start = 0
    max_length = 1

    for end in range(1, len(trail)):
        if abs(trail[end] - trail[end - 1]) > k:
            # Find the correct start index for the next valid hike
            while start < end and abs(trail[end] - trail[start]) > k:
                start += 1
        
        max_length = max(max_length, end - start + 1)

    return max_length

# Example usage
trail = [4, 2, 1, 4, 3, 4, 5, 8, 15]
k = 3
print(longest_hike(trail, k))  # Output: 8