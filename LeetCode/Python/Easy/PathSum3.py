""" 437. Path Sum III
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root is None: return 0
        # go left include root
        leftRoot = Solution.sumPaths(self, root.left, sum - root.val)
        # go left not include root
        left = Solution.pathSum(self, root.left, sum)
        # go right include root
        rightRoot = Solution.sumPaths(self, root.right, sum - root.val)
        # go right not include root
        right = Solution.pathSum(self, root.right, sum)
        # check val
        return leftRoot + left + rightRoot + right + 1 if root.val == sum else leftRoot + left + rightRoot + right
        # return
        
    def sumPaths(self, root: TreeNode, sum: int) -> int:
        if root is None: return 0
        #go left
        left = Solution.sumPaths(self, root.left, sum - root.val)
        #go right
        right = Solution.sumPaths(self, root.right, sum - root.val)
        #check self
        return left + right + 1 if root.val == sum else left + right