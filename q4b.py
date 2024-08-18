class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def largestBSTSubtreeSum(root):
    def helper(node):
        if not node:
            return True, 0, float('inf'), float('-inf')
        
        left_is_bst, left_sum, left_min, left_max = helper(node.left)
        right_is_bst, right_sum, right_min, right_max = helper(node.right)
        
        if left_is_bst and right_is_bst and left_max < node.val < right_min:
            current_sum = node.val + left_sum + right_sum
            max_sum[0] = max(max_sum[0], current_sum)
            return True, current_sum, min(left_min, node.val), max(right_max, node.val)
        
        return False, 0, 0, 0

    max_sum = [0]
    helper(root)
    return max_sum[0]

# Example usage:
# Construct the binary tree:
#       1
#      / \
#     4   3
#    / \   \
#   2   4   2
#            \
#             5
#            / \
#           4   6

root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(2)
root.right.right.right = TreeNode(5)
root.right.right.right.left = TreeNode(4)
root.right.right.right.right = TreeNode(6)

print(largestBSTSubtreeSum(root))  # Output: 20

