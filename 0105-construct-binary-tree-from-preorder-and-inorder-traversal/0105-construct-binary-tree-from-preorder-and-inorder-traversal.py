# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        """
        1. Took the first value of preorder -> root
        2. Find the root in inorder
        3. everything left of the root is left subtree, everything right of root is right subtree
        4. Do the same thing for each subtree.
        """

        if not preorder:
            return None
        
        root = TreeNode(preorder[0])

        #Find the index of root in inorder
        #Everything left of inorder goes to left subtree
        #Everything right of mid goes to right subtree
        mid = inorder.index(root.val)

        #in preorder list mid tells us how many left elements should be part of that subtree 

        preorder_left = preorder[1:mid+1]
        #Every element after mid+1 should be part of right
        preorder_right = preorder[mid+1:]

        #Inorder left every element to the elft of root

        inorder_left = inorder[:mid]
        inorder_right = inorder[mid+1:]

        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        return root