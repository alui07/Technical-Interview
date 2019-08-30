/* 108. Convert Sorted Array to Binary Search Tree
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:
Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
 */

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        if (nums.length == 0) return null;
        if (nums.length == 1) return new TreeNode(nums[0]);
        int middle = nums.length/2;
        TreeNode root = new TreeNode(nums[middle]);
        root.left = insert(Arrays.copyOfRange(nums, 0, middle));
        root.right = insert(Arrays.copyOfRange(nums, middle+1, nums.length));
        return root;
    }
    public TreeNode insert(int[] nums) {
        if (nums.length == 0) return null;
        if (nums.length == 1) return new TreeNode(nums[0]);
        int middle = nums.length/2;
        TreeNode root = new TreeNode(nums[middle]);
        if (middle >= 0) root.left = insert(Arrays.copyOfRange(nums, 0, middle));
        if (middle + 1 <= nums.length) root.right = insert(Arrays.copyOfRange(nums, middle+1, nums.length));
        return root;
    }
}