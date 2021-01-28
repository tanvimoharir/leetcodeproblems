# 701. Insert into a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def insert(root,val):
    if not root:
        return TreeNode(val)
    if root.val>val:
        root.left=insert(root.left,val)
    else:
        root.right=insert(root.right,val)
    return root
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        return insert(root,val)
