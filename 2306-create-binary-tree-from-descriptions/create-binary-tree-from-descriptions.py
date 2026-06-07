# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()

        for p, c, isLeft in descriptions:

            if p not in nodes:
                nodes[p] = TreeNode(p)

            if c not in nodes:
                nodes[c] = TreeNode(c)

            if isLeft:
                nodes[p].left = nodes[c]
            else:
                nodes[p].right = nodes[c]

            children.add(c)

        for p in descriptions:
            if p[0] not in children:
                return nodes[p[0]]

        