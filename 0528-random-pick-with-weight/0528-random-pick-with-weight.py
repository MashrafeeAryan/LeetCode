import random
class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []        
        self.total = 0
        for nums in w:
            self.total+=nums
            self.prefix_sum.append(self.total)
    def pickIndex(self) -> int:
        """"
        We will do a bianry search
        """
        target = random.randint(1, self.total)
        left = 0
        right = len(self.prefix_sum) -1

        while left < right:
            mid = (left+right)//2

            if self.prefix_sum[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return right
            
    

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()