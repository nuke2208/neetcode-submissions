# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        def depth(root,level):
            if root is None:
                return
            if level == len(result):
                result.append([])
            result[level].append(root.val)
            depth(root.left,level+1)
            depth(root.right,level+1)
        depth(root,0)
        return result
        