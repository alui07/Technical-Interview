""" 113. Path Sum II
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # general DFS solution, return all possible paths that match the sum
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root is None: return []
        if root.left is None and root.right is None and root.val == sum: return [[sum]]
        
        leftList, rightList = [], []
        if root.left is not None: 
            leftList = Solution.pathSum(self, root.left, sum-root.val)
            Solution.insertVal(self, leftList, root.val)
        if root.right is not None: 
            rightList = Solution.pathSum(self, root.right, sum-root.val)
            Solution.insertVal(self, rightList, root.val)
        leftList.extend(rightList)
        return leftList
    
    # ex: [
    #       [5,2,1,3,5,6],
    #       [1,2,3,4,5,6]
    #     ]
    #
    # and insert 10
    #
    #     [
    #       [10,5,2,1,3,5,6]
    #       [10,1,2,3,4,5,6]
    #     ]
    def insertVal(self, path: List[List[int]], val: int):
        for i in range(len(path)):
            path[i].insert(0, val)