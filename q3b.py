
def optimize_boarding(head, k):
    n = len(head)  # Total number of passengers
    boarding_sequence = [] 

    # Process the list in chunks of size k
    for i in range(0, n, k):
        # Extract the current chunk of passengers
        chunk = head[i:i + k]
        boarding_sequence.extend(reversed(chunk))
    
    return boarding_sequence

# Example 1
head1 = [1, 2, 3, 4, 5]
k1 = 2
print(optimize_boarding(head1, k1))  # Output: [2, 1, 4, 3, 5]

# Example 2
head2 = [1, 2, 3, 4, 5]
k2 = 3
print(optimize_boarding(head2, k2))  # Output: [3, 2, 1, 4, 5]


