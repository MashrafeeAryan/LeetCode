# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        """
        U: We are checking if binary tree is symmetric. We basicaly seeing if left and irght nodes are equal
        M: BFS seems the easiet way we can match each level
        P: 
        We use queue = deque([root]) because we want to sue FIFO
        2. while queue to see if any elements inque
        3. We poleft the frist elmenet
        4. if leftnode.val == right node.val, we move on
        5. we add both nodes to queue.
        6. so it will take the left one. do a left and right but it wont work then. becaause it is going deep in the left side. we need another pointer to go the righth side as well
        """

        if root is None:
            return True

        queue = deque([(root.left, root.right)])

        while queue:
            
            #this wont make sense for root
            left_node, right_node = queue.popleft()

            if left_node is None and right_node is None:
                continue

            if left_node is None or right_node is None:
                return False
            if left_node.val != right_node.val:
                return False
            
            # technically we do not need to check it, it will be checked in later turn
            #but we also do not want bunch of Nones
            queue.append((left_node.left, right_node.right))
            queue.append((left_node.right, right_node.left))

        return True

