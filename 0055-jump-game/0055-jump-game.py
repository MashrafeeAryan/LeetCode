class Solution:
    def canJump(self, nums: list[int]) -> bool:
        """
        U: Each value in array gives us possible values we cn use to get to the end index. we do not need to use the maximum value
        """

        farthest = 0

        for index in range(len(nums)):
            if index > farthest:
                return False
            
            farthest = max(farthest, index+nums[index])

        return True