# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        # 左节点递归
        if root.left:
            root.left = self.trimBST(root.left, L, R);

        # 右节点递归
        if root.right:
            root.right = self.trimBST(root.right, L, R);

        if root.val >= L and root.val <= R:
            # 节点值在指定范围内
            return root
        elif root.val < L:
            # 节点值小于指定范围
            return root.right
        elif root.val > R:
            # 节点值大于指定范围
            return root.left
