# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # 广度优先搜索
        def BFS(nodes):
            """
            :type nodes: [TreeNode...]
            :rtype: int
            """

            firstNode = nodes[0]
            result = firstNode.val

            nextRowNodes = []

            for node in nodes:

                if node.left:
                    nextRowNodes.append(node.left)

                if node.right:
                    nextRowNodes.append(node.right)

            if len(nextRowNodes) == 0:
                return result
            else:
                return BFS(nextRowNodes)

        result = root.val

        nodes = []
        if root.left:
            nodes.append(root.left)

        if root.right:
            nodes.append(root.right)

        if len(nodes) == 0:
            return root.val
        else:
            return BFS(nodes)
