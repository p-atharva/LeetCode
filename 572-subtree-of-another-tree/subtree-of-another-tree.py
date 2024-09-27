# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #if subroot is NULL, it is a subtree of root
        if not subRoot:
            return True

        #if root is NULL, then we compare subRoot with it
        if not root:
            return False
        
        #checking if the immediate root structure is same as subRoot
        if self.isSame(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    #Helper function (Leetcode is same tree)    
    def isSame(self, r, sR):
        if not r and not sR:
            return True
        if not r or not sR or r.val != sR.val:
            return False

        return (self.isSame(r.left, sR.left) and self.isSame(r.right, sR.right))
        