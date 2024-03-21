# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def getMinimumDifference(self, root):
        if not root:
            return 0

        min_diff = [float('inf')]

        def helper(node):
            if not node:
                return float('inf')

            left_diff = helper(node.left)
            right_diff = helper(node.right)

            curr_diff = abs(node.val - left_diff)
            min_diff[0] = min(min_diff[0], curr_diff)
            curr_diff = abs(node.val - right_diff)
            min_diff[0] = min(min_diff[0], curr_diff)

            return node.val

        helper(root)

        return min_diff[0]


sol = Solution()
root = [4,2,6,1,3]
result = sol.getMinimumDifference(root)
print(result)  # Output: 1
