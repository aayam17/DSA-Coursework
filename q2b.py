from sortedcontainers import SortedList

def canSitTogether(nums, indexDiff, valueDiff):
    sorted_list = SortedList()
    
    for i, num in enumerate(nums):
        # Remove elements that are out of the sliding window
        if sorted_list and i - sorted_list[0][1] > indexDiff:
            sorted_list.pop(0)
        
        # Check for valid pairs in the sorted list
        pos = sorted_list.bisect_left((num - valueDiff, -1))
        if pos < len(sorted_list) and abs(sorted_list[pos][0] - num) <= valueDiff:
            return True
        
        # Insert the current number into the sorted list
        sorted_list.add((num, i))
    
    return False

# Example usage
nums = [2, 3, 5, 4, 9]
indexDiff = 2
valueDiff = 1

print(canSitTogether(nums, indexDiff, valueDiff))  # Output: True
