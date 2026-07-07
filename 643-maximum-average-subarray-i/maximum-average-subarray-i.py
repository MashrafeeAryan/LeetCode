class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = sum(nums[:k])
        maxAvg = window/k

        for right in range(k, len(nums)):
            window -= nums[right - k]
            window += nums[right]
            maxAvg = max(window/k, maxAvg)
        
        return maxAvg