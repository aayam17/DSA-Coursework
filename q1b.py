def rotate_char(c, direction):
    if direction == 1:  # Rotate character clockwise
        return chr((ord(c) - ord('a') + 1) % 26 + ord('a'))
    elif direction == 0:  # Rotate character counter-clockwise
        return chr((ord(c) - ord('a') - 1) % 26 + ord('a'))

def apply_shifts(s, shifts):
    s = list(s)  # Convert string to list for easy manipulation
    
    for start, end, direction in shifts:  # Apply each shift in the given list of shifts
        for i in range(start, end + 1):
            s[i] = rotate_char(s[i], direction)
    
    return ''.join(s)  # Convert the list back to a string

# Example usage
s = "hello"
shifts = [[0, 1, 1], [2, 3, 0], [0, 2, 1]]
result = apply_shifts(s, shifts)
print(result)  # Output: "jglko"

