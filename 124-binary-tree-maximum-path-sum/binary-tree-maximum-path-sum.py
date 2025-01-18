# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #global result to compare with the max path
        result = [root.val]

        #using DFS approach with recursion
        def dfs(root):
            #checking if we have a root or not
            if not root:
                return 0

            #suppose we have, recursively calculate max value for left & right
            left = dfs(root.left)
            right = dfs(root.right)

            #if they have -ve values we don't want, so take max of the val & 0
            left = max(left, 0)
            right = max(right, 0)

            #now calculate the total path sum & compare with prev calulated
            result[0] = max(result[0], root.val + left + right)

            #return only the max val sum without splitting
            return root.val + max(left, right)

        dfs(root)
        return result[0] 