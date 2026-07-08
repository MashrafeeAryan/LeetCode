class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        totalSum = 0
        minLength = float('inf')
        left = 0
        for right in range(len(nums)):
            totalSum+=nums[right]
            while totalSum >= target:
                minLength = min(minLength, right-left+1)
                totalSum-=nums[left]
                left+=1
        if minLength == float("inf"):
            return 0
        return minLength