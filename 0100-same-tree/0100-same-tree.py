# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        """
        U: We are returning true only if the nodes strcuture and value are the same. otherwise it is false
        M: BFS because we can match each level but i am not sure why dfs will be a bad option
        P: Maybe the brute force method would be to check both at the same time.
        So a bfs search with queues for both of them but as we do that one question arises.
        So both queues should be the exact same. we can probalby create both queues. then a for loop to comapre the vals of both queues nodes
        """

        queue = deque([(p,q)])

        while queue:
            p_node, q_node = queue.popleft()
            if p_node == None and q_node == None:
                continue
            if p_node == None or q_node == None:
                return False

            if p_node.val != q_node.val:
                return False
            
            queue.append((p_node.left, q_node.left))
            
            queue.append((p_node.right, q_node.right))
        
        return True