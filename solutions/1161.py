# 1161. Maximum Level Sum of a Binary Tree
# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        queue = deque([root])
        ans = (-2147483648, -2147483648)
        level = 0
        while queue:
            level += 1
            sums = 0
            for i in range(len(queue)):
                node = queue.popleft()
                sums += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans = max(ans, (sums, level), key=lambda x: x[0])
        return ans[1]
