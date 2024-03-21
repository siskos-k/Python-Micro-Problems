

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # Helper function to count nodes
        def countNodes(node):
            if not node:
                return 0
            return 1 + countNodes(node.left) + countNodes(node.right)

        if not root:
            return None

        count = countNodes(root.left) + 1

        if k == count:
            return root.val
        elif k < count:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k - count)
