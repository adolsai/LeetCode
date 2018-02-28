class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums:
            maxNumber = max(nums)
            maxNumberIndex = nums.index(maxNumber)

            node = TreeNode(nums[maxNumberIndex])

            node.left = self.constructMaximumBinaryTree(nums[:maxNumberIndex])

            node.right = self.constructMaximumBinaryTree(nums[maxNumberIndex + 1:])

            return node
