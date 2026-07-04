class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Sliding window problem
        1. We first find the average of the list till k and store it
        2. We then write a for loop from k to len(nums)
        3. When we are changing window, we just mutliply the current average by k and then add the latest addition tot he window. And subtract the oldest element in the window

        """

        window = sum(nums[:k])
        maxAvg = window/k

        for right in range(k, len(nums)):
            window += nums[right]
            window -= nums[right-k]

            maxAvg = max(maxAvg, window/k)

        return maxAvg