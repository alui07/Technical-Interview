""" 101. Symmetric Tree
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Note:
Bonus points if you could solve it both recursively and iteratively.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None: return True;
        return Solution.compare(self, root.left, root.right);
        
    def compare(self, n1,n2):
        if n1 == None and n2 == None: return True;
        if n1 == None or n2 == None: return False;
        if (Solution.compare(self, n1.left, n2.right) and Solution.compare(self, n1.right, n2.left) and n1.val == n2.val): return True;
        
        return False;