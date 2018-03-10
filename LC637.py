# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        def BFS(nodes, averageNums):

            nextLevelNodes = []

            nodeValueSum = 0

            for node in nodes:
                nodeValueSum += node.val

                if node.left:
                    nextLevelNodes.append(node.left)

                if node.right:
                    nextLevelNodes.append(node.right)

            averageNums.append(nodeValueSum / float(len(nodes)))

            if len(nextLevelNodes) == 0:
                return averageNums
            else:
                return BFS(nextLevelNodes, averageNums)

        return BFS([root], [])

