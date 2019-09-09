/* 102 Binary Tree Level Order Traversal
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
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
    public List<List<Integer>> levelOrder(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        List<List<Integer>> tree = new ArrayList<List<Integer>>();
        queue.add(root);
        List<Integer> list = new ArrayList<Integer>();
        
        int limit = 1, curr_nodes = 0, next_nodes = 0;
        while (queue.peek() != null) {
            TreeNode curr = queue.poll();
            if(curr.left != null) queue.add(curr.left);
            else next_nodes++;
            if(curr.right != null) queue.add(curr.right);
            else next_nodes++;
            curr_nodes++;
            list.add(curr.val);
            if (curr_nodes >= limit) {
                curr_nodes = next_nodes;
                next_nodes *= 2;
                limit *= 2;
                tree.add(list);
                list = new ArrayList<Integer>();
            }
        }
        return tree;
    }
}