def most_utilized_classroom(n, classes):
    # Step 1: 
    classes.sort(key=lambda x: (x[0], -x[2]))
    
    # Step 2: 
    room_end_times = [0] * n
    room_class_counts = [0] * n
    
    # Step 3: 
    for start, end, students in classes:
        earliest_room = 0
        for i in range(1, n):
            if room_end_times[i] < room_end_times[earliest_room]:
                earliest_room = i
        
        if room_end_times[earliest_room] <= start:
            room_end_times[earliest_room] = end
        else:
            room_end_times[earliest_room] += (end - start)
        
        room_class_counts[earliest_room] += 1
    
    # Step 4: 
    max_classes = max(room_class_counts)
    for i in range(n):
        if room_class_counts[i] == max_classes:
            return i

# Example Usage
n1 = 2
classes1 = [[0, 10, 30], [1, 5, 25], [2, 7, 20], [3, 4, 10]]
print(most_utilized_classroom(n1, classes1))  # Output: 0

n2 = 3
classes2 = [[1, 20, 30], [2, 10, 25], [3, 5, 20], [4, 9, 15], [6, 8, 10]]
print(most_utilized_classroom(n2, classes2))  # Output: 1
