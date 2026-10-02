# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        """
    	U: We are trying to find the maximum depth of a binary tree from root to the very end
        M: DFS and backtracking
        P: we will have a max value. It doesnt make sense to use DFS because you will just go in and then go  up and then try another way. that wont help us count. we can probalby do breadth first search we check every level. so how many elements at firrst level how many at second
        """

        if not root:
            return 0

        queue = deque([root])
        depth = 0
        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            depth+=1
        
        return depth