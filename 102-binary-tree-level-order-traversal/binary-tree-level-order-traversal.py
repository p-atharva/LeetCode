# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        final_list = []
        que = collections.deque()

        if root:
            que.append(root)

        while que:
            level_list = []
            
            for i in range(len(que)):
                node = que.popleft()
                level_list.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            final_list.append(level_list)
        return final_list
        


        